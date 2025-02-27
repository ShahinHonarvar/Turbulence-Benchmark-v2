from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(lst):
    anagram_count = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_count[sorted_word].append(word)
    count = 0
    for group in anagram_count.values():
        if len(group) > 1:
            count += len(list(combinations(group, 2)))
    return count >= 219