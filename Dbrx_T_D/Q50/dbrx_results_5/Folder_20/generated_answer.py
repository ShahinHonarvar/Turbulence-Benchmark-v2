import re
from collections import Counter

def if_contains_anagrams(words):
    anagrams = []
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams.append(sorted_word)
    anagram_counts = Counter(anagrams)
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) >= 64