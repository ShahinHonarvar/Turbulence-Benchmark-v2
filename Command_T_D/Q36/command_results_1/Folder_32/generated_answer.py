import re

def filter_chars(s):
    return re.sub('(?<=.)[A-F0-9]{%d,%d}(?=.)' % (40, 63), '', s)