import re

def filter_chars(s):
    return re.sub('[0-9][\\w-]{0,51}[0-9]', '\x01', s)