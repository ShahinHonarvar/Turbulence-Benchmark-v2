import re

def filter_chars(str):
    return re.sub('[H-e]', '', str)