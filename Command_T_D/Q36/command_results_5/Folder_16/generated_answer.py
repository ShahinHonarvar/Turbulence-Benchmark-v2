import re

def filter_chars(string):
    return re.sub('[A-Z][^_]{%d}{%d}'.format(331, 713), '', string)