import re

def filter_chars(s):
    return re.sub('(?i)([1-9]s)', '', s)