import re

def filter_chars(s):
    return re.sub('[\\w_][=A-E]', '', s)