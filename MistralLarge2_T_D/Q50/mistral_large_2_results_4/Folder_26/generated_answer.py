from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    anagram_pairs = sum((1 for group in anagram_dict.values() if len(group) > 1 for _ in combinations(group, 2)))
    return anagram_pairs >= 49