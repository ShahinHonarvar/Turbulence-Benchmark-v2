from collections import Counter

def if_contains_anagrams(strings):
    anagram_groups = {}
    for s in strings:
        lower_s = s.lower()
        if len(lower_s) < 3:
            continue
        key = tuple(sorted(Counter(lower_s).items()))
        if key not in anagram_groups:
            anagram_groups[key] = []
        anagram_groups[key].append(s)
    anagram_pairs = 0
    for group in anagram_groups.values():
        anagram_pairs += len(group) * (len(group) - 1) // 2
    return anagram_pairs <= 36