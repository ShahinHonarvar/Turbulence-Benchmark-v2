import re

def filter_chars(s):
    return re.sub('([A-E])\\d{3}', '\x01', s)