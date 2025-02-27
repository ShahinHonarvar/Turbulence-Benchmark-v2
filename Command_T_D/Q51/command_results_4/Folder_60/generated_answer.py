import re

def if_contains_anagrams(lst):
    return bool(re.findall('(?i)(?=.*?[a-z]{3}){2}(?=.*?[a-z]{3})', lst))