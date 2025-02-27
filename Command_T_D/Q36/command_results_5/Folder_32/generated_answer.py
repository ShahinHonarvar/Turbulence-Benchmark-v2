import re

def filter_chars(s):
    return re.sub('[a-h][40-63]', '', s)