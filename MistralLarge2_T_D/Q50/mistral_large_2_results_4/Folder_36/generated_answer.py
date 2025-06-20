from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_dict[sorted_string].append(string)
    anagram_pairs_count = 0
    for anagram_list in anagram_dict.values():
        if len(anagram_list) > 1:
            anagram_pairs_count += len(list(combinations(anagram_list, 2)))
    return anagram_pairs_count >= 312