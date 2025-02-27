import re

def filter_chars(s):
    return re.sub('(?<=\\d{3})[/=8]', '', s)