import re

def filter_chars(s):
    return re.sub('[a-z]$', '', s, flags=re.I)