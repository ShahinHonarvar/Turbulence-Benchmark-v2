from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for s in string_list:
        cleaned_s = ''.join(filter(str.isalpha, s.lower()))
        if len(cleaned_s) >= 3:
            sorted_s = ''.join(sorted(cleaned_s))
            anagram_dict[sorted_s].append(s)
    anagram_pairs = 0
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            anagram_pairs += len(list(combinations(anagrams, 2)))
            if anagram_pairs > 70:
                return False
    return True