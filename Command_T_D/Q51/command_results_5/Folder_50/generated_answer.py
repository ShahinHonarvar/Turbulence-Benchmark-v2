import re

def if_contains_anagrams(s):
    return not bool(re.findall('(.)\x01', ''.join(sorted(s, key=lambda x: x.lower()))))