from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        str_dict[sorted_word].append(word)
    anagram_count = 0
    for anagram_list in str_dict.values():
        for a, b in combinations(anagram_list, 2):
            if len(a) >= 3 and len(b) >= 3 and (a.lower() == b.lower()):
                anagram_count += 1
    return anagram_count >= 16