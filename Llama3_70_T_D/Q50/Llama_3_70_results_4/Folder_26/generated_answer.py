from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_count = 0
    anagrams_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams_dict[sorted_string].append(string)
    for anagrams in anagrams_dict.values():
        if len(anagrams) > 1:
            anagram_count += len(list(combinations(anagrams, 2)))
    return anagram_count >= 49