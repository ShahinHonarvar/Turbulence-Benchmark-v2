import re

def if_contains_anagrams(s):
    return bool(re.findall('<(.*?)>', s))