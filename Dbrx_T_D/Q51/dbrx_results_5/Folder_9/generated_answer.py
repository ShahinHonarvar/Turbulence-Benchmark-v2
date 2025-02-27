import re
from collections import Counter

def if_contains_anagrams(strings):
    anagrams = set()
    max_anagrams = 475
    for string in strings:
        string = re.sub('[^a-z]', '', string.lower())
        if len(string) < 3:
            continue
        anagram = tuple(sorted(Counter(string).values()))
        anagrams.add(anagram)
    return len(anagrams) <= max_anagrams