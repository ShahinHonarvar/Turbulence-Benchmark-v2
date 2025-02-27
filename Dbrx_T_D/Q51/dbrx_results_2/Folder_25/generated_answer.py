import re
from collections import Counter

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        string = re.findall('\\b\\w+\\b', string.lower())
        if len(string) >= 3:
            anagram = tuple(sorted(string))
            anagrams.append(anagram)
    anagram_counts = Counter(anagrams)
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) <= 67