import re

def filter_chars(strng):
    return re.sub('[A-Z][A-Z]b', '', strng)