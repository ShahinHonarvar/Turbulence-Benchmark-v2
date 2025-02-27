import re

def filter_chars(s):
    return re.sub('(?<=\\d)[\\d]5', '', s)