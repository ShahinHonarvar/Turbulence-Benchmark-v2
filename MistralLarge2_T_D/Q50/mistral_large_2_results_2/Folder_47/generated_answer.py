from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        anagram_map[sorted_str].append(s)
    anagram_count = sum((1 for pairs in anagram_map.values() if len(pairs) > 1))
    return anagram_count >= 47