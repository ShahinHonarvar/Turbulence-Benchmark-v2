import re

def filter_chars(str):
    return re.sub('_ge_o', '', str)