import re

def filter_chars(s):
    return re.sub('[A-Z][^A-Z]{%d,%d}'.format(63, 84), '', s)