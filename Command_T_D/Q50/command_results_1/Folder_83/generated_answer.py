import re

def if_contains_anagrams(texts):
    texts = re.findall('(?i)(?=([a-z]+)\x01)', ''.join(texts))
    return len(texts) >= 48