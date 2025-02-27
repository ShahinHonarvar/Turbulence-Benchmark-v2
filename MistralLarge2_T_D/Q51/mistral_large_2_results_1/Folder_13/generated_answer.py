from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    count = 0
    for s in strings:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        anagrams[key].append(s)
    for group in anagrams.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
    return count <= 54