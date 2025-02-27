from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    pairs = 0
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_map[sorted_str].append(s)
    for anagram_list in anagram_map.values():
        n = len(anagram_list)
        pairs += n * (n - 1) // 2
        if pairs > 206:
            return False
    return True