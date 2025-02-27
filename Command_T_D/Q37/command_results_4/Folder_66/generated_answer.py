import re

def filter_chars(s):
    return re.sub('(c[0-9A-Z]i)', '', s)