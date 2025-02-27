import re

def filter_chars(text):
    return re.sub('[A-Z][\\d]{%d,%d}'.format(27, 85), '', text)