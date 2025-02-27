import re

def filter_chars(s):
    return re.sub('([A-Z])([0-9])([A-Z])', '\x02\x01\x03', s)