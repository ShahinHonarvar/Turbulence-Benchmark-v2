from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_map = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_chars = tuple(sorted(string.lower()))
            anagram_map[sorted_chars] += 1
    for count in anagram_map.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count <= 16