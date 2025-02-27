import re

def filter_chars(s):
    return re.sub('(?<=.)[A-Z][a-z]{%d,%d}'.format(41, 86), '', s)