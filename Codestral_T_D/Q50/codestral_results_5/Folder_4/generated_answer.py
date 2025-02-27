from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagrams[''.join(sorted(s.lower()))].append(s)
    return sum((len(a) > 1 for a in anagrams.values())) >= 42