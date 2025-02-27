import re

def filter_chars(s):
    return re.sub('[A-Z][^A-Z]{%d,%d}'.format(17, 63), '', s)