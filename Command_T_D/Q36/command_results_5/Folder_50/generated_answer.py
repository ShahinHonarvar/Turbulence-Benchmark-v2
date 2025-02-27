import re

def filter_chars(s):
    return re.sub('[^a-z]{%d,%d}'.format(ord('%') - 1, ord('q') - 1), '', s)