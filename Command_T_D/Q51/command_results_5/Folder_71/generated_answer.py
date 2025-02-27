import re

def if_contains_anagrams(s):
    return not re.findall('(?=([A-Z]+[A-Z][A-Z]?)[A-Z])', s)