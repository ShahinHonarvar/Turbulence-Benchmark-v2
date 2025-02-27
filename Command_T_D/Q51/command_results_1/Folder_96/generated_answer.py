import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?:\\w){3}([a-z])\x01', s))