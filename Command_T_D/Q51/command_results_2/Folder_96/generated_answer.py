import re

def if_contains_anagrams(list1):
    return bool(re.findall('(?i)([a-z])\x01+', ' '.join(list1), flags=re.I))