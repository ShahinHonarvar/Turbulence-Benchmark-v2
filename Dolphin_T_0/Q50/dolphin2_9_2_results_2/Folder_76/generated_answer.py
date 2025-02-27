from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in map(str.lower, lst):
        if len(word) >= 3:
            c.update(Counter(word))
    pairs = 0
    for v in c.values():
        if v >= 3:
            pairs += v * (v - 1) // 2
    return pairs >= 143