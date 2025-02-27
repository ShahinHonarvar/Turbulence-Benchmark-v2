import re

def filter_chars(s):
    return re.sub('[A-z]{%d,%d}'.format(318, 337), '', s)