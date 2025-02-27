from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) < 3 or len(set(word.lower())) < 3:
            continue
        c.update(Counter(sorted(word.lower())))
    pairs = 0
    for key in c:
        pairs += c[key] * (c[key] - 1) // 2
    return pairs