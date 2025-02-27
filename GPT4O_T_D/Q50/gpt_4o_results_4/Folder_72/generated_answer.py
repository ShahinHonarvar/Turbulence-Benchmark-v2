from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(int)
    for s in strings:
        normalized = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagram_map[normalized] += 1
    pair_count = 0
    for count in anagram_map.values():
        if count >= 2:
            pair_count += count * (count - 1) // 2
    return pair_count >= 55