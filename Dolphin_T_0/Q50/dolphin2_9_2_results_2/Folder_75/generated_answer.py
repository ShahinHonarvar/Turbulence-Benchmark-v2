from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) >= 3:
            c[tuple(sorted(word.lower()))] += 1
    pairs = sum(((x - 1) // 2 for x in c.values() if x > 1))
    return pairs >= 70