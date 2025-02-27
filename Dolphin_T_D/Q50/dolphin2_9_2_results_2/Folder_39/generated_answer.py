from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    c = Counter()
    for word in lst:
        if len(word) >= 3:
            w = ''.join(sorted(word.lower()))
            c[w] += 1
    pairs = 0
    for v in c.values():
        pairs += v * (v - 1) // 2
    return pairs >= 54