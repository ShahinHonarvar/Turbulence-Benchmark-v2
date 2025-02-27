import re
from collections import Counter

def if_contains_anagrams(words):
    max_pairs = 116
    anagrams = []
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams.append(sorted_word)
    anagram_counts = Counter(anagrams)
    pair_count = sum((count // 2 for count in anagram_counts.values() if count > 1))
    return pair_count <= max_pairs