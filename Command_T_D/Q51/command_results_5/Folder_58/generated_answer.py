import re

def if_contains_anagrams(s):
    return bool(re.findall('(?=([A-Z])\x01+)(?=\\D\x01+)(?=\\D[A-Z]\x01+)', s))