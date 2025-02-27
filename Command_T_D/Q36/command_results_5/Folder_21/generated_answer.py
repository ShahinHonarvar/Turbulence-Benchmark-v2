import re

def filter_chars(s):
    return re.sub('(?i)([2-6])', '\x01', s)