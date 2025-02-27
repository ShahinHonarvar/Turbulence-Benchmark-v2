import re

def filter_chars(s):
    return re.sub('([A-Z])\\d{3}([A-Z])', '\x01\x02', s)