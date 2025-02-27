from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_map[sorted_str].append(string)
    pair_count = 0
    for anagrams in anagram_map.values():
        n = len(anagrams)
        if n > 1:
            pair_count += n * (n - 1) // 2
        if pair_count > 14:
            return False
    return True