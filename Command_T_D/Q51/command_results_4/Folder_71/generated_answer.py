import re

def if_contains_anagrams(texts):
    anagrams = set(re.findall('(?i)([A-Z])\x01+', texts))
    return len(anagrams) <= 9