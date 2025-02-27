import re

def filter_chars(str):
    return re.sub('[A-Z][^j]{%d}{%d}'.format(31, 73), '', str)