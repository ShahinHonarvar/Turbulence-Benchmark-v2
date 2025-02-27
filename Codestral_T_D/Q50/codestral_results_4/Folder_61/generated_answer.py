from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagram_groups[''.join(sorted(s.lower()))].append(s)
    anagram_pairs = 0
    for group in anagram_groups.values():
        if len(group) >= 2:
            anagram_pairs += len(group) * (len(group) - 1) // 2
    return anagram_pairs >= 8