from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_map[sorted_str] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_map.values()))
    return pairs >= 57