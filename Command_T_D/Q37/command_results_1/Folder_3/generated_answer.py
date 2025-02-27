import re

def filter_chars(s):
    return re.sub('[A-Z][A-Z0-9_]*6[A-Z0-9_]{%d,%d}'.format(37, 56), '', s)