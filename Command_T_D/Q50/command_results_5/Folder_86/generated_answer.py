import re

def if_contains_anagrams(strs):
    return bool(re.findall('(?i)(?=.*[a-z])\x01+', strs, flags=re.I))