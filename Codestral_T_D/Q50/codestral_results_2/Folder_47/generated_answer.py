from collections import defaultdict

def if_contains_anagrams(strings):
    groups = defaultdict(list)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            groups[sorted_s].append(s)
    count = 0
    for group in groups.values():
        if len(group) >= 2:
            count += len(group) * (len(group) - 1) // 2
    return count >= 47