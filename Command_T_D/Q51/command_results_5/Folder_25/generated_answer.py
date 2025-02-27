import re

def if_contains_anagrams(texts):
    return len(re.findall('<(.*?)>', texts)) <= 67