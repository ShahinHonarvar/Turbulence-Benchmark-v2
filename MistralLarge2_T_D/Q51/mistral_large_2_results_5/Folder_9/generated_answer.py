from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    sorted_strings = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            sorted_strings[sorted_string].append(string)
    anagram_pairs = sum((len(lst) * (len(lst) - 1) // 2 for lst in sorted_strings.values()))
    return anagram_pairs <= 475