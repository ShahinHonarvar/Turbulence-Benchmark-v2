import re

def filter_chars(string):
    return re.sub('[A-z][^A-i]', '', string)