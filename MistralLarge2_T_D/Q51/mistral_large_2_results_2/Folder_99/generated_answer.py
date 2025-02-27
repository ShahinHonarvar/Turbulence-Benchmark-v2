from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_count[sorted_word] += 1
    anagram_pairs = 0
    for count in anagram_count.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 93