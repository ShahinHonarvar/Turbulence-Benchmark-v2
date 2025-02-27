import re

def filter_chars(s):
    return re.sub('[4567]', '', s)