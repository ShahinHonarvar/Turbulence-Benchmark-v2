import re

def filter_chars(text):
    return re.sub('[A-Z]{%d,%d}'.format(309, 591), '', text)