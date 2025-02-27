import re

def if_contains_anagrams(s):
    return not re.findall('(?i)([A-Z][a-z][A-Z][a-z]?)', s, flags=re.I)