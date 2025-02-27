from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(set)
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            anagrams[sorted_str].add(string)
    pairs = 0
    for anagram_set in anagrams.values():
        pairs += len(anagram_set) * (len(anagram_set) - 1) // 2
    return pairs <= 14