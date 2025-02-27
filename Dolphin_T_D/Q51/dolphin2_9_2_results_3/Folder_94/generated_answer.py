from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for s in lst:
        if len(s) >= 3:
            c[tuple(sorted(s.lower()))] += 1
    return all((num <= 181 for num in c.values()))