from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_map[sorted_s] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_map.values()))
    return anagram_pairs <= 289