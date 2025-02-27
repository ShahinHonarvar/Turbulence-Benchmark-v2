import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(\\S+)(?:\x01)', ' '.join(s), flags=re.I))