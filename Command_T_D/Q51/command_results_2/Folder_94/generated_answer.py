import re

def if_contains_anagrams(s):
    return bool(re.findall('(?=([A-Z]\\d{2})[A-Z][A-Z]\\d{2})\x01', s))