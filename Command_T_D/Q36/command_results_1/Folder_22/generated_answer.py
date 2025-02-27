import re

def filter_chars(s):
    return re.sub('[a-z]', '', s[55:-1])