from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(lst):
    anagrams_count = 0
    anagrams_map = defaultdict(list)
    for s in lst:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        if len(s_lower) >= 3:
            s_sorted = ''.join(sorted(s_lower))
            anagrams_map[s_sorted].append(s_lower)
    for anagrams in anagrams_map.values():
        anagrams_count += len(list(combinations(anagrams, 2)))
    return anagrams_count <= 48