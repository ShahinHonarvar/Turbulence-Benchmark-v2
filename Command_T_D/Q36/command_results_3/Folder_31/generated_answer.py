import re

def filter_chars(s):
    return re.sub('c[0-9]d', '', s)