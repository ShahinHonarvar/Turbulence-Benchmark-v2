import re

def filter_chars(s):
    return re.sub('([^aK]{%d,%d})' % (18, 95), '', s)