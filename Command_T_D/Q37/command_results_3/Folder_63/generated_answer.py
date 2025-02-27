import re

def filter_chars(s):
    return re.sub('(?i)[/a]{%d,%d}'.format(42, 92), '', s)