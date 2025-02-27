import re

def filter_chars(s):
    return re.sub('[A-Z]{%d,}'.format(31), '', s)