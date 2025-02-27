import re

def filter_chars(s):
    return re.sub('[A-Z]{%d,%d}{%d,%d}' % (20, 62, i, k), '', s)