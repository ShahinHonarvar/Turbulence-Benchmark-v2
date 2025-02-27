import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?:(?P<s>[A-Z])\x01)+\x01\x01+)+', s))