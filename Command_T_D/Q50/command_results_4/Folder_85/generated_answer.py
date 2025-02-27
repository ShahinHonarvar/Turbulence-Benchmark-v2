import re

def if_contains_anagrams(texts):
    return bool(re.findall('(?i)(\\S{3})\x01', texts))