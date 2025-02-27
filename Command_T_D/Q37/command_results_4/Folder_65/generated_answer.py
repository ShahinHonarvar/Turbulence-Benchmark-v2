import re

def filter_chars(s):
    return re.sub('[A-Z][a-z]00[@]', '', s)