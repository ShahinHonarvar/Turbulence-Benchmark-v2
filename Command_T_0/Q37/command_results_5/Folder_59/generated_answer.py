import re

def filter_chars(s):
    return re.sub('(?<=.)\\d_', '', s)