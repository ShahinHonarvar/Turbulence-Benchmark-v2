import re

def if_contains_anagrams(texts):
    res = re.findall('(?=([a-z0-9]+)\x01)', texts, flags=re.I)
    return len(res) >= 155