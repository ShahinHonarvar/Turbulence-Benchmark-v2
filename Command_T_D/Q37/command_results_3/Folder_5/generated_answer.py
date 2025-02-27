import re

def filter_chars(s):
    return re.sub('[A-Z]{%d,%d}{%d,%d}' % (24, 82, 5, '<'), '', s)