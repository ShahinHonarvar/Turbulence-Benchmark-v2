import re

def filter_chars(s):
    return re.sub('([^,]*)[A-V]', '\x01', s)