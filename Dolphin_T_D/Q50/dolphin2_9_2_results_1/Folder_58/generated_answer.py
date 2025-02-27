from collections import Counter

def if_contains_anagrams(lst):
    count = len([s for s in lst if len(s) >= 3])
    sorted_strings = Counter([tuple(sorted(s.lower())) for s in lst if len(s) >= 3])
    pairs = 0
    for key, value in sorted_strings.items():
        pairs += value * (value - 1) // 2
    return pairs >= 411