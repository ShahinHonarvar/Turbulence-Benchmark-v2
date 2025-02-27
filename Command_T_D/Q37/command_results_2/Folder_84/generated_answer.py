import re

def filter_chars(str):
    return re.sub('[6-9][A-Z]', '', str)