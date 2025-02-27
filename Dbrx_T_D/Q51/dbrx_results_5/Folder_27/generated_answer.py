import re
from collections import Counter

def if_contains_anagrams(words):
    anagrams = []
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams.append(sorted_word)
    anagram_counts = Counter(anagrams)
    return sum((v * (v - 1) // 2 for v in anagram_counts.values())) <= 113