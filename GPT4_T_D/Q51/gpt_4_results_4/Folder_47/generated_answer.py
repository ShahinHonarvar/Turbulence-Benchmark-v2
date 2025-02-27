from collections import Counter
from itertools import combinations

def if_contains_anagrams(lst):
    sorted_words = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    counts = Counter(sorted_words)
    anagram_pairs = sum((val * (val - 1) // 2 for val in counts.values()))
    return anagram_pairs <= 366