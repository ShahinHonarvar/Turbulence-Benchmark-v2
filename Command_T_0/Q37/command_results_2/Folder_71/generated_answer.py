import re

def filter_chars(s):
    return re.sub('[0-9][A-Z][a-z]{%d,%d}'.format(32, 46), '', s)