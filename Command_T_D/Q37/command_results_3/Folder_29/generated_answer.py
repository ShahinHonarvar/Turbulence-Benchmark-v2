import re

def filter_chars(s):
    return re.sub('[&\\d]:[&v]{%d,%d}'.format(12, 88), '', s)