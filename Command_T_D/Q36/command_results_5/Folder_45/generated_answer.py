import re

def filter_chars(s):
    return re.sub('(?i)([A-Z])([81-86])([A-Z])', '\x01!', s)