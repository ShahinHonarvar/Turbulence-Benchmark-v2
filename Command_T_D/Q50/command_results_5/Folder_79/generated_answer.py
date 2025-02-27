import re

def if_contains_anagrams(texts):
    return bool(re.findall('(?i)(?=([a-z]+)\x01)', texts, flags=re.I))