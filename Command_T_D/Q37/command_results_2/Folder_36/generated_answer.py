import re

def filter_chars(s):
    return re.sub('(\\d+,){9}\\d+)', '', s)