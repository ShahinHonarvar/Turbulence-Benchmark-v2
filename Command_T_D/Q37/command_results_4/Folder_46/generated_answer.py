import re

def filter_chars(s):
    return re.sub('([A-Z])\\d{3}([A-Z])', '\x01\\d\x02', s)