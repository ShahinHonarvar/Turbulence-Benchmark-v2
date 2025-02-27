from collections import defaultdict

def if_contains_anagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagrams[sorted_s].append(s)
    count = 0
    for anagram_list in anagrams.values():
        if len(anagram_list) > 1:
            count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return count <= 318