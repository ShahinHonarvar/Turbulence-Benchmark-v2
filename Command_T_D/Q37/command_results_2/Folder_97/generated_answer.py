import re

def filter_chars(s):
    return re.sub('[D-u]{%d,%d}'.format(227, 235), '', s)