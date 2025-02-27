import re

def filter_chars(s):
    return re.sub('[g-z]', '', s)