from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for s in str_list:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagrams[s].append(s)
    pairs = 0
    for anagram_group in anagrams.values():
        if len(anagram_group) > 1:
            pairs += len(anagram_group) * (len(anagram_group) - 1) // 2
    return pairs <= 15