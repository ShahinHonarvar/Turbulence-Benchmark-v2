import re

def filter_chars(s):
    return re.sub('[A-Z]{%26,80}', '', s)