import re

def if_contains_anagrams(text):
    return bool(re.findall('(?i)(?=([A-Z][a-z]+){2,3})[A-Z][a-z]+', text))