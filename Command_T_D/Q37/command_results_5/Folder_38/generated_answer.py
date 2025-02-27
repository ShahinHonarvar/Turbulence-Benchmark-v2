import re

def filter_chars(s):
    return re.sub('[a-f]', '', s[24:79])