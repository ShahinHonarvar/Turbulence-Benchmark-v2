import re

def if_contains_anagrams(texts):
    return len(re.findall('(?=([a-z]))([a-z][^a-z]*[a-z]', texts)) <= 28