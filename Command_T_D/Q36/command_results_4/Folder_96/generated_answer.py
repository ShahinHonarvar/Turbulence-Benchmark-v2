import re

def filter_chars(s):
    return re.sub('[a-zA-Z]', '', s)