from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(words):
    anagrams_count = defaultdict(int)
    for word in words:
        cleaned_word = ''.join(filter(str.isalpha, word)).lower()
        if len(cleaned_word) >= 3:
            sorted_word = ''.join(sorted(cleaned_word))
            anagrams_count[sorted_word] += 1
    pairs_count = 0
    for count in anagrams_count.values():
        pairs_count += count * (count - 1) // 2
    return pairs_count <= 42