import re

def filter_chars(s):
    return re.sub('[\\d@qwertyuiop]', '', s)