import re

def filter_chars(s):
    return re.sub('([a-zA-Z])[2-3]', '\x01', s)