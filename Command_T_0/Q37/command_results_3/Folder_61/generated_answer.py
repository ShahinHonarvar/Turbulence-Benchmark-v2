import re

def filter_chars(s):
    return re.sub('[G-p]', '', s, flags=re.I)