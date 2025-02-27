from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) >= 3 and len(word) <= 10:
            c[tuple(sorted(word.lower()))] += 1
    pairs = 0
    for v in c.values():
        pairs += v * (v - 1) // 2
    return pairs >= 50