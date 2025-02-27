from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(str_list):
    char_count_dict = defaultdict(int)
    for string in str_list:
        if len(string) < 3:
            continue
        char_count_dict[''.join(sorted(string.lower().replace(' ', '')))] += 1
    anagram_pairs = 0
    for count in char_count_dict.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 66