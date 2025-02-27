import re

def filter_chars(s):
    return re.sub('([\\w]+)\\W{35}(\\w)+\\W{40}\\W{35}(\\w)+\\W{40}(.)+', '\x01 \x03 \x04', s)