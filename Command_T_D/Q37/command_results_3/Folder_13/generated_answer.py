import re

def filter_chars(s):
    return re.sub('[0-8].*?[0-9].*?[a-s]', '', s)