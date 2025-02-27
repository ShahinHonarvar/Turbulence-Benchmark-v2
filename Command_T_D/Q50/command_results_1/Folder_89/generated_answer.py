import re

def if_contains_anagrams(s):
    return len(re.findall('(?i)(?P<x>.+)\x01', s)) >= 36