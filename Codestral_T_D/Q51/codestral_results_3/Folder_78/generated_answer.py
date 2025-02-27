from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        lower_s = ''.join(sorted(s.lower()))
        if len(lower_s) >= 3:
            anagrams[lower_s].append(s)
    count = 0
    for group in anagrams.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
    return count <= 70