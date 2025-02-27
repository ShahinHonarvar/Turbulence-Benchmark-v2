from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams_map = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        anagrams_map[key].append(s)
    anagram_pairs_count = sum((len(lst) // 2 for lst in anagrams_map.values() if len(lst) > 1))
    return anagram_pairs_count <= 25