from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_map = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            anagram_map[key] += 1
    for count in anagram_map.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count >= 246