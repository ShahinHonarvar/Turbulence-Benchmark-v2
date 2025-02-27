from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(int)
    count = 0
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_map[sorted_s] += 1
    for count in anagram_map.values():
        pairs = count * (count - 1) // 2
        if pairs >= 68:
            return True
    return False