import re

def filter_chars(s):
    return re.sub('[A-Za-z]+', '', s[56:-86])