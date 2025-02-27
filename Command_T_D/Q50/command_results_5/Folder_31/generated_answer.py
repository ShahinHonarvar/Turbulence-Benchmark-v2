import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?P<text>[a-z]+)\x01', s))