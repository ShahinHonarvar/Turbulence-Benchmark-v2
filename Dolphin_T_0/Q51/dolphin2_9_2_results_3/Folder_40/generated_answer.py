from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) < 3:
            continue
        c[tuple(sorted(word.lower()))] += 1
    for v in c.values():
        if v > 2:
            return False
    return True