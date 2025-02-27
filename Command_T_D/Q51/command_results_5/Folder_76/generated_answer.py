import re

def if_contains_anagrams(s):
    return not re.findall('(?i)(?:(?P<a>[a-z])\x01+){2,}(?P<b>[a-z])\x01+)+', s)