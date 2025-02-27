import re

def if_contains_anagrams(s):
    return not re.findall('(?=([A-Z])\x01)', s, flags=re.I)