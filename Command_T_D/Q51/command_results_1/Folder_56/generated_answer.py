import re

def if_contains_anagrams(s):
    return bool(re.findall('([A-Z]+[a-z]+)+', s, flags=re.I))