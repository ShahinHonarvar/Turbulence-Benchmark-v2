from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for s in str_list:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagrams[sorted_s].append(s)
    pairs = 0
    for anagram_group in anagrams.values():
        pairs += len(anagram_group) * (len(anagram_group) - 1) // 2
    return pairs >= 34