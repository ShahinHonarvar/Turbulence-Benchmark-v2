import re

def if_contains_anagrams(s):
    return bool(re.findall('(?=([a-z]+){3}[A-Z][a-z]?)\x01', ''.join(s), re.I))