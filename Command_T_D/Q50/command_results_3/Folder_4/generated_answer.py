import re

def if_contains_anagrams(text):
    res = len(re.findall('(?i)(?P<x>[A-Z][^A-Z]?)\x01', text)) >= 42
    return res