import re

def filter_chars(s):
    return re.sub('[A-Z][^A-Z]{%d,%d}'.format(13, 40), '', s)