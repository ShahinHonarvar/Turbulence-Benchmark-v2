from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        anagram_map[sorted_s].append(s)
    anagram_count = sum((1 for group in anagram_map.values() if len(group) >= 2))
    return anagram_count >= 29