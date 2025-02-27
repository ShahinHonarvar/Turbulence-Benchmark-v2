import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?P<s>[a-z]{3})\x01', s))