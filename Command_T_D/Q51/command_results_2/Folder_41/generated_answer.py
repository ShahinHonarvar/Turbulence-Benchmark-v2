import re

def if_contains_anagrams(text):
    anagrams = re.findall('(?=([A-Z][A-Z][A-Z]))([A-Z][A-Z]{{3}})', text.lower())
    return len(anagrams) <= 52