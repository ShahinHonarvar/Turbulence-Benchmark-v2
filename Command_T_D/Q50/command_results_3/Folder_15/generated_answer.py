import re

def if_contains_anagrams(lst):
    return bool(re.findall('(?i)(?:(?P<a>[a-z]{3})[a-z]{2})\x01', lst))