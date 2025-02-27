import re

def if_contains_anagrams(texts):
    return bool(re.findall('(\\A[a-z]+){2}\\Z', texts))