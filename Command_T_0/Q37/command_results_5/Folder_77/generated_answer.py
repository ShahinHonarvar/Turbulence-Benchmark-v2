import re

def filter_chars(s):
    return re.sub('[0-7]{%d,%d}'.format(384, 411), '', s)