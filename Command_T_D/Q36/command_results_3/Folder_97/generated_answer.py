import re

def filter_chars(str):
    return re.sub('[A-Z][^m]{%d,%d}'.format(309, 591), '', str)