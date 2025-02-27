import re

def filter_chars(s):
    return re.sub('[A-Q]{%d,%d}'.format(38, 99), '', s)