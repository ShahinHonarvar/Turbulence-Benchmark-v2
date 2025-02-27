import re

def filter_chars(s):
    return re.sub('[6-9][0-9]A', '', s)