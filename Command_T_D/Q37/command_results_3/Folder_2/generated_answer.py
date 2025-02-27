import re

def filter_chars(s):
    return re.sub('(([A-Z]{%d,%d})%s)' % (477, 984, '|'), '', s)