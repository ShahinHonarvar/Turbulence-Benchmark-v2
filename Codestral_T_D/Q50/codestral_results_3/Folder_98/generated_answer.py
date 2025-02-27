from collections import defaultdict

def if_contains_anagrams(strings):
    groups = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            groups[''.join(sorted(s.lower()))].append(s)
    return sum([len(g) >= 7 for g in groups.values()]) >= 1