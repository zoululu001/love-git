/*可任意修改样式，或恢复预设值，保存后生效
相对“默认样式”而作的修改会用  红色 标注*/
/*塘主微信：tangzhubox*/
/*转载请注明出处*/

.output_wrapper/*此属性为全局*/
{
     font-size: 16px;      /*字体大小*/
     color: #3e3e3e;      /*字体颜色*/
     line-height: 1.8;      /*行高*/
     word-spacing:0px; /*增加或减少单词间的空白（即字间隔）*/
     letter-spacing:0px;/*增加或减少字符间的空白(字符间距)*/
     font-family: "Helvetica Neue",Helvetica,"Hiragino Sans GB","Microsoft YaHei",Arial,sans-serif;   
}
.output_wrapper *
{
  font-size: inherit  ;
  color: inherit;
  line-height: inherit;
  margin:0px;
  padding:0px;
}

p {/*段落*/
  margin: 1.5em 0px;     /*行间距以及首行缩进像素距离*/
}
h1,h2,h3,h4,h5,h6 {      /*1~6号标题*/
  margin: 1.5em 0px;
  font-weight:bold;        /*标题字体加粗bold，不加粗normal*/
}
h1 {
  font-size: 1.6em  ;
}
h2 {
  font-size: 1.4em;
}
h3 {
  font-size: 1.3em;
}
h4 {
  font-size: 1.2em;
}
h5 {
  font-size: 1em;
}
h6 {
  font-size: 1em;
}



h2 /*增加对h2标题属性的修改*/
{
  font-size: 1.3rem;
  border-bottom: 2px solid rgb(239, 112, 96);
}
h2 span {
 display: inline-block;
 font-weight: bold;
 background: rgb(239, 112, 96);
 color: #ffffff;
 padding: 3px 10px 1px;
 border-top-right-radius: 3px;
 border-top-left-radius: 3px;
 margin-right: 3px;
}
h2:after {
 display: inline-block;
 content: "";
 vertical-align: bottom;
 border-bottom: 36px solid #efebe9;
 border-right: 20px solid transparent;
}

h3/*增加对h3标题属性的修改*/
{
  //border-bottom: 2px solid rgb(63,63,63);     /*标题下划线*/
  text-align: center !important;  /*center居中，left左对齐，right右对齐*/
  margin-bottom:35px;
  font-size: 16px;                           /*16像素字体大小*/
}
h3 span{/*增加对h3标题字体的修改*/
  display:inline-block;
  background: rgb(63,63,63);         /*深灰色背景*/
  color:#ffffff;                                   /*白色字体*/
  padding:  10px  16px;
  border-radius:10px;                     /*边框添加圆角*/
  box-shadow: 5px 5px 10px black;/*黑色阴影*/
}

ul, ol {
  padding-left: 32px;
}
ul{ /*无序列表*/
    list-style-type: disc;     /*disc默认实心圆，circle空心圆，square方块*/
    color:#1e6bb8;
margin-left: -0.5em;          /*引用竖线与左边框的距离*/
}
ol { /*有序列表*/
  list-style-type:decimal;   /*decimal阿拉伯数字，upper-roman大写罗马数字，lower-alpha*/
  color:#1e6bb8;
margin-left: -0.5em;       /*引用竖线与左边框的距离*/
}
li *  
{
 /*color: #3e3e3e;*/
} 

li{  /*在公众号下，改变不了li符号的属性（如颜色），并会影响其子元素的属性;而在其它博客平台中，则能正常使用*/ 
    margin-bottom: 0.5em;
/*  color:#159957; */    
}
.code_size_default  /*代码块默认size*/
{
  line-height: 18px;
  font-size: 14px; 
  font-weight:normal;
  word-spacing:0px; 
  letter-spacing:0px; 
}
.code_size_tight /*代码块紧凑size*/
{
   line-height: 15px; 
   font-size: 11px; 
   font-weight:normal;
   word-spacing:-3px; 
   letter-spacing:0px; 
}
pre code /*代码块*/
{           
     font-family: Consolas, Inconsolata, Courier, monospace;
     border-radius: 15px;         /*圆形边框*/
}

/*orangeheart引用*/
/*blockquote {
  display: block;
  font-size: 0.9em;
  overflow: auto;
  overflow-scrolling: touch;
  border-left: 3px solid rgb(239, 112, 96);
  color: #6a737d;
  padding: 10px 10px 10px 20px;
  margin-bottom: 20px;
  margin-top: 20px;
  background: #fff9f9;
}
blockquote p {
  margin: 0px;
  line-height: 26px;
}*/



blockquote { /*大佬排版引用块*/
 display: block;                  /*block方块，none不显示，inline*/
  padding: 1em 15px ;         /*文字到引用竖线的距离*/
  font-size: 0.9em;
  padding-right: 15px;
  margin: 1em 0;                   /*行间距*/
  color: #819198;                  /*字体颜色*/
  border-left: 4px solid #009688;  /*引用竖线宽度及颜色，solid实线，dashed虚线*/
  background: #f2f7fb;         /*引用方框颜色*/
  overflow: auto;
  overflow-scrolling: touch; 
  word-wrap: normal;
  word-break: normal;  
  margin-left: 1.5em;           /*引用竖线与左边框的距离*/
}
blockquote p {
    margin: 0px;            /*引用线上下边框*/
}

a { /*超链接*/
  text-decoration: none;
  color: #1e6bb8;
  word-wrap:break-word;
}

strong  /*强调*/
{
  font-weight: bold;
color: #BF360C;
}
em /*斜体*/
{
 font-style:italic;/*italic斜体，normal正常*/
color: #00ACC1;
}
del /*删除线*/
{
 font-style:italic;
}
strong em/*强调的斜体*/
{
font-weight: bold;
}

hr {  /*分隔线*/

  border-bottom: 2px solid #BF360C ; /*分割线的线宽及颜色*/
  margin: 1em auto;                         /*分割线行间距*/

}

code /*行内代码*/
{
    word-wrap: break-word;
    padding: 2px 4px;
    border-radius: 4px;
    margin:0 2px;
    color:#e96900;
    background:#f8f8f8;
}
img
{
  display: block;
  margin:0 auto;  /*图片水平居中*/
  /* margin:0 0;  */ /*图片水平居左，如需要请打开*/
  max-width:100%;
}
figcaption/*图片描述文字*/
{
  margin-top:10px;
  text-align:center;
   /* text-align:left;  */ /*当图片水平居左时，请打开*/
  color:#999;
  font-size: 0.7em;
}


/*================表格开始================*/
table {
  padding: 0;
  border-collapse: collapse;
  border-spacing: 0;
  font-size: 1em;
  font: inherit;
  border: 0;
  margin: 0 auto;
}

tbody {
  margin: 0;
  padding: 0;
  border: 0;
}

table tr {
  border: 0;
  border-top: 1px solid #CCC;
  background-color: white;
  margin: 0;
  padding: 0;
}

table tr:nth-child(2n) {
  background-color: #F8F8F8;
}

table tr th, table tr td {
  font-size: 16px;
  border: 1px solid #CCC;
  margin: 0;
  padding: 5px 10px;
}

table tr th {
  font-weight: bold;
  color: #eee;
  border: 1px solid #009688;
  background-color: #009688;
}
/*================表格结束================*/



/*================数学公式开始================*/
.katex-display {/*块公式*/
  font-size:1.22em; 
}
.katex
{/*行内公式*/
  padding:8px 3px;
}
.katex-display > .katex
{/*块公式*/
   display:inline-block;
   text-align:center;
   padding:3px;
}
.katex img
{/*行内公式对应的图片*/
  display:inline-block;
  vertical-align:middle;
}
/*================数学公式结束================*/

a[href^="#"] sup
{/*注脚*/
  vertical-align:super;
  margin:0 2px;  
  padding:1px 3px; 
  color: #ffffff;
  background:#666666;
  font-size:0.7em;
}

/*================任务列表开始================*/
.task-list-list {
  list-style-type: none;
}
.task-list-list.checked {/*已完成*/
  color: #3e3e3e;
}

.task-list-list.uncheck {/*未完成*/
  color: #bfc1bf;
}
.task-list-list .icon_uncheck, .task-list-list .icon_check {
  display: inline-block;
  vertical-align: middle;
  margin-right: 10px;
}
.task-list-list .icon_check:before
{/*已完成*/
    content: "√";
    border: 2px solid #3e3e3e;
    color:red;
}
.task-list-list .icon_uncheck:before
{/*未完成*/
   content: "x";
   border: 2px solid #bfc1bf;
    color: #bfc1bf;
}
.task-list-list .icon_check:before, .task-list-list .icon_uncheck:before
{/*标志框*/
  padding:2px;
  padding-left: 5px;
  padding-right: 8px;
  border-radius:5px;
}
/*================任务列表结束================*/

.toc
{/*总目录*/
  margin-left:25px;
}
.toc_item
{/*每条目录*/