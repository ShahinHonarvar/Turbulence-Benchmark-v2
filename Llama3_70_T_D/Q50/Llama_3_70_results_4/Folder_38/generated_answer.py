from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagrams_count = 0
    anagrams_dict = defaultdict(list)
    for string in strings:
        lower_string = string.lower()
        sorted_string = ''.join(sorted(lower_string))
        if len(string) >= 3:
            anagrams_dict[sorted_string].append(lower_string)
    for anagrams in anagrams_dict.values():
        if len(anagrams) > 1:
            anagrams_count += len(list(combinations(anagrams, 2)))
    return anagrams_count >= 24