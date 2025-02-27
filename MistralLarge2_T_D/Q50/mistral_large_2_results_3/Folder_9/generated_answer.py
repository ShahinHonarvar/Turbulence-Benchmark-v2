from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_map = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        anagram_map[sorted_s].append(s)
    for key in anagram_map:
        if len(anagram_map[key]) > 1:
            pairs = len(anagram_map[key]) * (len(anagram_map[key]) - 1) // 2
            anagram_count += pairs
    return anagram_count >= 66