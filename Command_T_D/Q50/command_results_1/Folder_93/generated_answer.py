import re

def if_contains_anagrams(s):
    return bool(re.findall('((?i)(?:(?P<x>.*[A-Z])\x01)+)', s))