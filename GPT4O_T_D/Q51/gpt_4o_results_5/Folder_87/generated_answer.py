from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_map[sorted_str].append(s)
    pairs_count = 0
    for anagram_list in anagram_map.values():
        n = len(anagram_list)
        if n > 1:
            pairs_count += n * (n - 1) // 2
        if pairs_count > 392:
            return False
    return True