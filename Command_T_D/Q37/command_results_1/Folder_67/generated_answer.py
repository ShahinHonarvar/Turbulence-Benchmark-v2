import re

def filter_chars(s):
    return re.sub('[[\\]]|t', '', s, flags=re.I)