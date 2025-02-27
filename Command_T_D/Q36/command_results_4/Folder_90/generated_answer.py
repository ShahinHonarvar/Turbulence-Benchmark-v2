import re

def filter_chars(s):
    return re.sub('[g-~]', '', s[344:-10])