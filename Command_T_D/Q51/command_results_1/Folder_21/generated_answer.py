import re

def if_contains_anagrams(texts):
    return bool(re.findall('(?i)(?=([a-z]+\\d){3}(?i)[a-z]+\\d){3})', texts))