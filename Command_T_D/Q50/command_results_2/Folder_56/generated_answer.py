import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?=([A-Z][a-z]{2,}(?:[A-Z][a-z]{2,})\x01)', s))