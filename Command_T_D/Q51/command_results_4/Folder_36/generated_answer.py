import re

def if_contains_anagrams(texts):
    return len(re.findall('(\\A[a-z]+[A-Z][a-z]?)\x01', texts)) <= 25