import re

def filter_chars(s):
    return re.sub('&[1-9][0-9]v', '', s)