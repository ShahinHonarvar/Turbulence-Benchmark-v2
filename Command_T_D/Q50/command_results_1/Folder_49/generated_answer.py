import re

def if_contains_anagrams(texts):
    return bool(re.findall('(?i)(?P<string>.*?[a-z])\x01', texts))