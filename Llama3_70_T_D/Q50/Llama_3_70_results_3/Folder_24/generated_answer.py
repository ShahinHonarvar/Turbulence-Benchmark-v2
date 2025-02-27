from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(strings):
    anagrams_count = 0
    strings = [''.join(sorted(s.casefold())) for s in strings if len(s) >= 3]
    anagrams_dict = defaultdict(list)
    for s in strings:
        anagrams_dict[s].append(s)
    for v in anagrams_dict.values():
        if len(v) > 1:
            anagrams_count += len(list(combinations(v, 2)))
    return anagrams_count >= 65