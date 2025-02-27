import re

def filter_chars(s):
    return re.sub('[2-\x84].[a-w]', '', s)