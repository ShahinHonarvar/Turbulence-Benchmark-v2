import re

def filter_chars(s):
    return re.sub('[Vv]..j', '', s)