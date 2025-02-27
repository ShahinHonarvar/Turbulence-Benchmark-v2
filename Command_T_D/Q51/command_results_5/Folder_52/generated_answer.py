import re

def if_contains_anagrams(texts):
    return bool(re.findall('(?i)(?=([a-z]+)\x01)', ''.join(map(str.lower, texts))))