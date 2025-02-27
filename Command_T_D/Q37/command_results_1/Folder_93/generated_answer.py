import re

def filter_chars(s):
    return re.sub('[Hef]([a-z])', '\x01', s)