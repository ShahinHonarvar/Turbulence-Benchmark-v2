import re

def filter_chars(s):
    return re.sub('[3-D]', '', s)