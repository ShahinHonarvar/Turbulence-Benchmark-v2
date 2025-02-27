from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_map[sorted_str].append(s)
    anagram_count = 0
    for group in anagram_map.values():
        n = len(group)
        if n > 1:
            anagram_count += n * (n - 1) // 2
        if anagram_count > 86:
            return False
    return True