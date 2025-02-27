from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_dict[sorted_string].append(string)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_dict.values() if len(group) > 1))
    return anagram_pairs >= 67