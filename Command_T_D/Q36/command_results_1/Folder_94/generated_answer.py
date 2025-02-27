import re

def filter_chars(s):
    return re.sub('(?i)([A-Z]?)[A-Z]?(\\d+)([A-Z]?)', '\x02', s)