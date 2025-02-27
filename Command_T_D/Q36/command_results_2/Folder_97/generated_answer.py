import re

def filter_chars(string):
    return re.sub('[A-Z][^A-Z]*[A-Z]', '', string)