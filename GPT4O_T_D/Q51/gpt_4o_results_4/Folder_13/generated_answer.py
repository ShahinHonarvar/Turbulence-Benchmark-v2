from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(int)
    count = 0
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_map[sorted_str] += 1
    for value in anagram_map.values():
        if value > 1:
            count += value * (value - 1) // 2
        if count > 54:
            return False
    return True