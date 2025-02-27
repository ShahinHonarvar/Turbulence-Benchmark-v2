import re

def filter_chars(s):
    return re.sub('[+\\d]{%d,%d}'.format(21, 43), '', s)