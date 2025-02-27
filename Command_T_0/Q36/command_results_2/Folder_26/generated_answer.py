import re

def filter_chars(s):
    return re.sub('[A-Z][^A-Z]{%d,%d}'.format(43, 83), '', s)