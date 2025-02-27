from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for s in lst:
        if len(s) >= 3:
            c[tuple(sorted(s.lower()))] += 1
    counts = list(c.values())
    return sum((count * (count - 1) // 2 >= 60 for count in counts))