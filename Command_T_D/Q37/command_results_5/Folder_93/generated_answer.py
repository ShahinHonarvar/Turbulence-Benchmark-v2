import re

def filter_chars(s):
    return re.sub('(?!<\\d).*(H[a-e])(?!\\d>).*(?!>).*(e[a-e])(?!\\d<).*(?!>)', '', s)