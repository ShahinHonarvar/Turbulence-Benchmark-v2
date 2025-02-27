from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_chars = ''.join(sorted(s.lower()))
            anagram_map[sorted_chars].append(s)
    anagram_pairs = 0
    for key in anagram_map:
        if len(anagram_map[key]) >= 2:
            anagram_pairs += len(anagram_map[key]) - 1
    return anagram_pairs >= 19