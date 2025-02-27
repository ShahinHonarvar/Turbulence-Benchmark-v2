from collections import defaultdict

def if_contains_anagrams(strings):
    groups = defaultdict(list)
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            groups[key].append(s)
    anagram_pairs = sum((len(g) * (len(g) - 1) // 2 for g in groups.values()))
    return anagram_pairs <= 72