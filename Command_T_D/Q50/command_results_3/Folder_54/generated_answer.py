import re

def if_contains_anagrams(texts):
    return bool(re.findall('(?i)(\\S+)(?:-\\d+)+', texts, flags=re.I))