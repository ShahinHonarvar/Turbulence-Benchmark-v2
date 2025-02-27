import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?P<s>.+?)\x01', s, flags=re.I))