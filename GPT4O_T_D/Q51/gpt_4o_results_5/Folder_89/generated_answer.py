from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_map[sorted_str] += 1
    anagram_pairs = 0
    for count in anagram_map.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs > 73:
                return False
    return True