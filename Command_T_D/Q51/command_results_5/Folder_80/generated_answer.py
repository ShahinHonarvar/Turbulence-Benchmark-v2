import re

def if_contains_anagrams(s):
    return bool(re.findall('(?=([A-Z]+[a-z]+[A-Z]+)+)', s, flags=re.I))