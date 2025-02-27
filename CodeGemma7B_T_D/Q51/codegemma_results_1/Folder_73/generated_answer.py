from itertools import combinations

def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        key = ''.join(sorted(string.lower()))
        if key not in anagrams or len(anagrams[key]) <= 2:
            anagrams[key] = anagrams.get(key, []) + [string]
    num_pairs = 0
    for anagram_group in anagrams.values():
        num_pairs += sum((pair in anagram_group for pair in combinations(anagram_group, 2)))
    return num_pairs <= 279