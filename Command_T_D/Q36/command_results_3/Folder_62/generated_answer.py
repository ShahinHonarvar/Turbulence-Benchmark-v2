import re

def filter_chars(s):
    return re.sub('(?i)[c-e][0-9]', '*', s)