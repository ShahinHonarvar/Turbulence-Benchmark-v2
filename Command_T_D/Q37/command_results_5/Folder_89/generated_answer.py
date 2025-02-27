import re

def filter_chars(s):
    return re.sub('[a-z][\\d]1', '', s)