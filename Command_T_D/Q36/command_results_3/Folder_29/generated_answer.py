import re

def filter_chars(s):
    return re.sub('[A-Z][^s]{%d}'.format(range(46, 68)), '', s)