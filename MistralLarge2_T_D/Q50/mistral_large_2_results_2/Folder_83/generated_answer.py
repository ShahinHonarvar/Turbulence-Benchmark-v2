from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            anagram_dict[key].append(word)
    count = 0
    for group in anagram_dict.values():
        if len(group) >= 2:
            count += len(list(combinations(group, 2)))
    return count >= 48