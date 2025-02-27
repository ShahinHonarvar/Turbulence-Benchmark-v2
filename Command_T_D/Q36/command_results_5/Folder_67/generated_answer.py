import re

def filter_chars(s):
    return re.sub('([a-z]{18,31})', '', s)