from collections import defaultdict

def if_contains_anagrams(strings):
    groups = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        groups[key].append(s)
    return any((len(v) >= 2 for v in groups.values()))