import re

def filter_chars(s):
    return re.sub('(?i)([A-Z])([2-9])', '\x01', s)