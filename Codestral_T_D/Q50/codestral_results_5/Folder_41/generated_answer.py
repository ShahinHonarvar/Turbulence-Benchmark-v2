from collections import Counter
    from math import comb

def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        string = string.lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            anagram_dict[sorted_string] = anagram_dict.get(sorted_string, 0) + 1
    pair_count = sum((comb(count, 2) for count in anagram_dict.values()))
    return pair_count >= 75