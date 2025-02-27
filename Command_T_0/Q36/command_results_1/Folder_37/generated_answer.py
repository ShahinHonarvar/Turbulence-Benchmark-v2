import re

def filter_chars(s):
    return re.sub('[0-5]', '', s)