from collections import defaultdict

def if_contains_anagrams(strs):
    lookup = defaultdict(list)
    for s in strs:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            lookup[sorted_s].append(s)
    count = 0
    for group in lookup.values():
        if len(group) >= 2:
            count += len(group) * (len(group) - 1) // 2
            if count >= 11:
                return True
    return False