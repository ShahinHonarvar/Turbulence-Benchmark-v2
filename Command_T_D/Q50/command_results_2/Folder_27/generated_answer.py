import re

def if_contains_anagrams(text):
    return len(re.findall('(?i)(?=([a-z]+[A-Z][a-z]?)\x01)', text)) >= 86