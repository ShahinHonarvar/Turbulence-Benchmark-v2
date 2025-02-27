from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_map[sorted_s] += 1
    anagram_pairs_count = 0
    for count in anagram_map.values():
        if count > 1:
            anagram_pairs_count += count * (count - 1) // 2
    return anagram_pairs_count <= 92