import re

def if_contains_anagrams(texts):
    return bool(re.findall('(?=([A-Z]+)([A-Z]+[a-z]+)+[A-Z]+)', texts))