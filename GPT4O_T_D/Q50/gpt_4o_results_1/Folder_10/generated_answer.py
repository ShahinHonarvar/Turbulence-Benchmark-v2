from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_map = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_map[sorted_string].append(string)
    for group in anagram_map.values():
        n = len(group)
        if n > 1:
            anagram_count += n * (n - 1) // 2
    return anagram_count >= 52