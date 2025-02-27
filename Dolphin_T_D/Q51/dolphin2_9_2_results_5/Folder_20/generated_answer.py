from collections import Counter

def if_contains_anagrams(strings):
    c = Counter()
    for s in strings:
        if len(s) >= 3:
            c[tuple(sorted(s.lower()))] += 1
    return 2 * sum((v * (v - 1) // 2 for v in c.values())) <= 131