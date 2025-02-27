import re

def filter_chars(s):
    return re.sub('[JQ]{%d,%d}'.format(88, 90), '', s)