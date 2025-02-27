import re

def filter_chars(s):
    return re.sub('[A-U]{%d,%d}' % (52, 81), '', s)