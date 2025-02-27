import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(\\d\\d)(?:\\d)(\\d)', ' '.join(s), flags=re.I))