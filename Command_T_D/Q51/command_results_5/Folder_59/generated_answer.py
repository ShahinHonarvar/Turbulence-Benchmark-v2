import re

def if_contains_anagrams(texts):
    return bool(re.findall('(?i)(?<=.)(.)\x01', texts))