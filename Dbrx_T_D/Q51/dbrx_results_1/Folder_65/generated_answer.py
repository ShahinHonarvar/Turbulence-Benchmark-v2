import re
from collections import Counter

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        string = re.sub('\\W+', '', string).lower()
        if len(string) >= 3:
            anagram = ''.join(sorted(string))
            anagrams.append(anagram)
    anagram_counts = Counter(anagrams)
    return sum(anagram_counts.values()) <= 72