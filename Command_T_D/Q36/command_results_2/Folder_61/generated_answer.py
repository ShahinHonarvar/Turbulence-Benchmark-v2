import re

def filter_chars(s):
    return re.sub('(?i)([A-E]?)', '\x01', s, flags=re.I)