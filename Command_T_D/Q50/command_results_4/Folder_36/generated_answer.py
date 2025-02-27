import re

def if_contains_anagrams(s):
    res = re.findall('((?:[a-z]){3})\x01', ''.join(s).lower())
    return len(res) >= 312