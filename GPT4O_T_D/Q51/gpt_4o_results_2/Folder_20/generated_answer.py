from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_map[sorted_s].append(s)
    anagram_pairs = 0
    for group in anagram_map.values():
        if len(group) > 1:
            n = len(group)
            anagram_pairs += n * (n - 1) // 2
    return anagram_pairs <= 131