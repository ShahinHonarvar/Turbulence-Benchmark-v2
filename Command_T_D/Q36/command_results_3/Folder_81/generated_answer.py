import re

def filter_chars(s):
    return re.sub('(?<=.)\\d\\d[a-f]', '', s)