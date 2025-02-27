import re

def filter_chars(s):
    return re.sub('(?i)[A-Z]\\d+', '', s)