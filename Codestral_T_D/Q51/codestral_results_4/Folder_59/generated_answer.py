from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagrams[''.join(sorted(s.lower()))].append(s)
    count = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values()))
    return count <= 15