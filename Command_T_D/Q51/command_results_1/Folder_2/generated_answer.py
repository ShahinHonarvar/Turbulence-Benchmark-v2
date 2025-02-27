import re

def if_contains_anagrams(texts):
    return bool(re.findall('(\\w+)(?:[A-Z])(\\w+)', texts))