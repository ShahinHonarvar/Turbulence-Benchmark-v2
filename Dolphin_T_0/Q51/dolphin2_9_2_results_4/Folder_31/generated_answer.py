from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) < 3:
            continue
        word = word.lower()
        c[tuple(sorted(word))] += 1
    return any((v > 2 for v in c.values()))