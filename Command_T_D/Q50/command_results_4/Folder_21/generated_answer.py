import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?:(?P<a>[a-z])\x01)+', s))