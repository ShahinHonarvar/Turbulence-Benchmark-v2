import re

def if_contains_anagrams(strs):
    return bool(re.findall('((?i)(?=([A-Z]))\x01)', strs, flags=re.I))