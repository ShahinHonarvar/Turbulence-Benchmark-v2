from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            s = ''.join(sorted(s.lower()))
            anagrams[s].append(s)
    count = sum((len(value) * (len(value) - 1) // 2 for value in anagrams.values()))
    return count >= 75