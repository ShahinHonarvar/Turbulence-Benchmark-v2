import re

def if_contains_anagrams(texts):
    return bool(re.findall('(?=([A-Z]+){3}([A-Z]+){3})', texts, flags=re.I))