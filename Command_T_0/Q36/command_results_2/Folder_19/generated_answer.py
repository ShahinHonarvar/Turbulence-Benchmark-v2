import re

def filter_chars(s):
    return re.sub('[;r]{%d,%d}'.format(77, 87), '', s)