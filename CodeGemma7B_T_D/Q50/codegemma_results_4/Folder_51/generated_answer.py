from itertools import combinations
        from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        str_dict[''.join(sorted(string))].append(string)
    anagram_count = 0
    for anagrams in str_dict.values():
        if len(anagrams) >= 3:
            anagram_count += combinations(anagrams, 2)
    return anagram_count >= 39