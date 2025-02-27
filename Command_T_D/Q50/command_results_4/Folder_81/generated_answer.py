import re

def if_contains_anagrams(a):
    return len(re.findall('<(.*?)>', re.findall('<(.*?)>', a))) > 15