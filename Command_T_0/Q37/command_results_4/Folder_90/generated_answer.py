import re

def filter_chars(s):
    return re.sub('[A-Z][a-z]{%d,%d}'.format(348, 852), '', s)