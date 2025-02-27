from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for word in str_list:
        word = ''.join(sorted(word.lower().replace(' ', '')))
        str_dict[word].append(word)
    anagram_count = 0
    for anagram_list in str_dict.values():
        if len(anagram_list) >= 3:
            anagram_count += len(list(combinations(anagram_list, 2)))
    return anagram_count <= 9