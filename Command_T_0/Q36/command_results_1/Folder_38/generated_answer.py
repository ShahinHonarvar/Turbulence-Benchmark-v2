import re

def filter_chars(s):
    return re.sub('[+\\d]{%d,%d}'.format(44, 48), '', s)