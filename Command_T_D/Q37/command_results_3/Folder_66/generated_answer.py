import re

def filter_chars(s):
    return re.sub('[cii]{%d,%d}'.format(27, 85), '', s)