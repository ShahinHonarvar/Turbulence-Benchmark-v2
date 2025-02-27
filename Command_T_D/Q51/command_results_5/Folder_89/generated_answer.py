import re

def if_contains_anagrams(lst):
    return bool(re.findall('(?i)([a-z]+)\x01', ' '.join(lst), flags=re.I))