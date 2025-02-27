import re

def filter_chars(s):
    return re.sub('([58-81])\x08', '\x01', s)