import re

def if_contains_anagrams(texts):
    return bool(re.findall('(?i)(?=([A-Z][A-Z0-9]+){2}\x01)', texts))