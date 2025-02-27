import re

def filter_chars(text):
    return re.sub('[>\\_]{%d,%d}'.format(521, 722), '', text)