from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_chars = ''.join(sorted(s.lower()))
            anagram_map[sorted_chars] += 1
    anagram_count = 0
    for count in anagram_map.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
        if anagram_count >= 233:
            return True
    return False