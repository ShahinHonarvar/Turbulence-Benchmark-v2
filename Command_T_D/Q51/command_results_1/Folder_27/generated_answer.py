import re

def if_contains_anagrams(text):
    return bool(re.findall('(?i)(?=([a-z]))([a-z][a-z][a-z])\x01', text))