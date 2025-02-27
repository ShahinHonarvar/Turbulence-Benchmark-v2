import re

def filter_chars(s):
    return re.sub('(?i)(?<=[X\\s])[a-z]', '', s)