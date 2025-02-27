import re

def if_contains_anagrams(s):
    return bool(re.findall('((?:[a-z]){3})\x01', s, flags=re.I))