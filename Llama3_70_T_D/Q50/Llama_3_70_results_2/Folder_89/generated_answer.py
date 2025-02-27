from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_count = 0
    sorted_strings = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            sorted_strings[sorted_string].append(string)
    for anagrams in sorted_strings.values():
        if len(anagrams) > 1:
            anagram_count += len(list(combinations(anagrams, 2)))
    return anagram_count >= 36