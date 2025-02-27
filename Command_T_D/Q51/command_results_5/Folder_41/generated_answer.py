import re

def if_contains_anagrams(s):
    return bool(re.findall('(?=([A-Z]+[a-z]+[A-Z]+[a-z]+))\x01', ' '.join(s), flags=re.I))