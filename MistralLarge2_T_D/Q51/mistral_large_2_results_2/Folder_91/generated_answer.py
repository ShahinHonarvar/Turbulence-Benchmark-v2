from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    anagram_pairs = 0
    for group in anagram_dict.values():
        if len(group) > 1 and len(group[0]) >= 3:
            anagram_pairs += len(list(combinations(group, 2)))
    return anagram_pairs <= 88