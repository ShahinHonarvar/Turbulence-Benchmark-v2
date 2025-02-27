import re

def filter_chars(s):
    return re.sub('[A-Z][A-Z0-9]@[A-Z0-9]p', '', s)