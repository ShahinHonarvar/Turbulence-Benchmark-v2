from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagrams[''.join(sorted(s.lower()))].append(s)
    count = 0
    for group in anagrams.values():
        if len(group) >= 3:
            count += 1
    return count >= 3