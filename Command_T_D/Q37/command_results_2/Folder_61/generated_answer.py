import re

def filter_chars(s):
    return re.sub('((?=G)[^Gp].)', '', s)