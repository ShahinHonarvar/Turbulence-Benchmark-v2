import re

def filter_chars(s):
    return re.sub('[A-Z][^_]{%d}{%d}'.format(48, 75), '', s)