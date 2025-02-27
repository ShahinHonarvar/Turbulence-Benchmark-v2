import re

def filter_chars(s):
    return re.sub('([a-z]{%d,%d})' % (23, 83), '', s)