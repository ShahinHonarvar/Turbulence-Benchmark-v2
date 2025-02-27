import re

def filter_chars(s):
    return re.sub('(?<=.)[A-Z]{%d,%d}{%d,%d}' % (40, 63, 7, 'H'), '', s)