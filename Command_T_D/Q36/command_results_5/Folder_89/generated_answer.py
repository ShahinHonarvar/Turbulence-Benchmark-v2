import re

def filter_chars(s):
    return re.sub('(?i)(?<=[a-z])[A-Z][^A-Z\\s)]', '\x01', s)