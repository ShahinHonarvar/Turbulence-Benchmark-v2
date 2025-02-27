import re

def filter_chars(text):
    return re.sub('[A-Z]{%d,%d}' % (477, 984), '', text)