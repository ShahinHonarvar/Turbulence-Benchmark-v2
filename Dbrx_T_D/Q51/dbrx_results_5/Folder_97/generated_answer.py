import re
from collections import Counter

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        string = re.sub('\\W+', '', string).lower()
        if len(string) >= 3:
            anagram = tuple(sorted(string))
            anagrams.append(anagram)
    anagram_counts = Counter(anagrams)
    return sum((value > 1 and value <= 18 for value in anagram_counts.values()))