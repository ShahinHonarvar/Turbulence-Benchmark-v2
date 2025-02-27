import re

def filter_chars(str):
    return re.sub('[A-g]43([A-g]C){8}69', '', str)