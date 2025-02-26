from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for s in string_list:
        sorted_s = ''.join(sorted(filter(str.isalpha, s.lower())))
        if len(sorted_s) >= 3:
            anagram_dict[sorted_s].append(s)
    anagram_pairs = sum((len(list(combinations(group, 2))) for group in anagram_dict.values() if len(group) > 1))
    return anagram_pairs <= 113