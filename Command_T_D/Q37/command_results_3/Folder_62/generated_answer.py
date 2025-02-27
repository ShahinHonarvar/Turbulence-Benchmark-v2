import re

def filter_chars(s):
    return re.sub('(I[a-z]{,8})', '', s)