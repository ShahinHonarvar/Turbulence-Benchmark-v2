from collections import defaultdict

def if_contains_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            groups[key].append(s)
    for group in groups.values():
        if len(group) >= 2:
            return True
    return False