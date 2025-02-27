import re

def filter_chars(s):
    return re.sub('([\\d_]+)(_+)', '\x01', s)