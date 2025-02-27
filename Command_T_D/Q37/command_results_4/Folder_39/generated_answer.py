import re

def filter_chars(s):
    return re.sub('[A-U][52-81]', '', s)