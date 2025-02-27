import re

def if_contains_anagrams(texts):
    return bool(re.findall('((?i)([A-Z])\x02)', texts, flags=re.I))