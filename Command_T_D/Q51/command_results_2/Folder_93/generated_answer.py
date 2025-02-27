import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?=([a-z]+[A-Z][a-z]?)\x01)+', ' '.join(s)))