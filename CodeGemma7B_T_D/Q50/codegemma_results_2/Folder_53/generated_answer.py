from itertools import combinations
from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for word in str_list:
        str_dict[' '.join(sorted(word))].append(word)
    anagrams_count = 0
    for anagrams in str_dict.values():
        if len(anagrams) >= 3:
            anagrams_count += len(list(combinations(anagrams, 2)))
    return anagrams_count >= 11