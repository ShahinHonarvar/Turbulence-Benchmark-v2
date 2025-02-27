import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?<=.)(.*?[A-Z])\x01', s, flags=re.I))