import re

def filter_chars(s):
    return re.sub('([\\d])\\d', '1\x01', s)