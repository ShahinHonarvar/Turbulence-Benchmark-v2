import re

def remove_repeat_chars(s):
    return re.sub('[A-Z][A-Z][A-Z][A-Z]', 'R', s)