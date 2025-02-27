import re

def filter_chars(s):
    return re.sub('[g-z]{%d,%d}'.format(344, 874), '', s)