from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    pairs = 0
    for word in lst:
        if len(word) >= 3:
            c[tuple(sorted(word.lower()))] += 1
    for v in c.values():
        if v >= 2:
            pairs += v * (v - 1) // 2
    return pairs <= 40