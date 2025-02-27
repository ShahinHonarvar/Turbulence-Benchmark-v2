import re

def filter_chars(string):
    return re.sub('[A-Z]', '', string)