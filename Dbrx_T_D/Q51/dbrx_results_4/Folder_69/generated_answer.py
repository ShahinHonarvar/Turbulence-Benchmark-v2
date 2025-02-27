import re
from collections import Counter

def if_contains_anagrams(strings):
    anagrams = set()
    for string in strings:
        string = re.sub('\\W+', '', string).lower()
        if len(string) < 3:
            continue
        anagram = ''.join(sorted(string))
        anagrams.add(anagram)
    return len(anagrams) <= 58