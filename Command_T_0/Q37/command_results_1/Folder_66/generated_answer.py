import re

def filter_chars(s):
    return re.sub('[c-i]', '', s)