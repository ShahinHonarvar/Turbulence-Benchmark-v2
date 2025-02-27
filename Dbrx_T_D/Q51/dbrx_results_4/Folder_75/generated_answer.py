import re

def if_contains_anagrams(lst):
    anagrams = set()
    for word in lst:
        letters = sorted(re.findall('[a-z]', word.lower()))
        anagram = ''.join(letters)
        anagrams.add(anagram)
    return len(anagrams) <= 55