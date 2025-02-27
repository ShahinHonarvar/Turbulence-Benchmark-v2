from collections import Counter

def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        key = tuple(sorted(Counter(s).items()))
        if key not in anagrams:
            anagrams[key] = 0
        anagrams[key] += 1
    return sum((v * (v - 1) // 2 for v in anagrams.values())) <= 64