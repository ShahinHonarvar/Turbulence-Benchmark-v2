from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for i in range(len(lst)):
        s = lst[i].lower()
        if len(s) >= 3:
            c[tuple(sorted(s))] += 1
    return sum((v == 2 for v in c.values())) <= 8