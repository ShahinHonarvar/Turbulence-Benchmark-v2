import re

def if_contains_anagrams(texts):
    return bool(re.findall('(?i)(?=.*[a-z])(?=.*[a-z][a-z]+)', texts))