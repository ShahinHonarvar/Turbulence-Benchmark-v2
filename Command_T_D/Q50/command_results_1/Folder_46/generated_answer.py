import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?:([a-z]){3})([a-z])\x01', ' '.join(s)))