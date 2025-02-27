import re

def filter_chars(s):
    return re.sub('([A-f])\\d{2}', '\x01', s)