import re

def if_contains_anagrams(lst):
    return bool(re.findall('(?i)(?=([a-z]{3}))([a-z]{3})([a-z]{3})', ' '.join(lst)))