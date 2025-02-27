import re

def filter_chars(str):
    return re.sub('[A-Z][/][0-5]', '', str)