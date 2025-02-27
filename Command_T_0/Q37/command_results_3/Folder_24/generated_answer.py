import re

def filter_chars(s):
    return re.sub('[a-z]{%d,%d}{%d,%d}' % (36, 79, 2, 's'), '', s)