import re

def filter_chars(s):
    return re.sub('([\\d_A-Z])[a-w]', '\x01', s)