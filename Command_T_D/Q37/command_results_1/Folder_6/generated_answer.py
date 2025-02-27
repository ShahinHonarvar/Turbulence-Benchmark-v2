import re

def filter_chars(s):
    return re.sub('[c,d,e,f,g,h,i,j,k,l,m,n]', '', s[13:-3])