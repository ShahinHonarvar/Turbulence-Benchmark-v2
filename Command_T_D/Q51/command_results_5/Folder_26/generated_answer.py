import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?<=.)(.*?[aeiou])\x01', ' '.join(s), flags=re.I))