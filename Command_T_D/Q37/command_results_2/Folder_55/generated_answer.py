import re

def filter_chars(s):
    return re.sub('(?<=.)\\$[a-z0-9];', '', s)