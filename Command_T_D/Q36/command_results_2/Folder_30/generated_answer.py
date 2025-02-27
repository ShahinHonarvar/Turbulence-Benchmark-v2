import re

def filter_chars(s):
    return re.sub('([A-Z]\\d){2,5}([A-Z])', '\x01', s)