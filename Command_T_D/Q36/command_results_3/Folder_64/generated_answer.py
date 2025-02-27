import re

def filter_chars(s):
    return re.sub('([\\d]+)3([\\d]+)[^7]', '\x01', s)