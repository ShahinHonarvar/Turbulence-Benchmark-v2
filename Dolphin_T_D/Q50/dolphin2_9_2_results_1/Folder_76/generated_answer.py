from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for w in lst:
        if len(w) >= 3:
            c[tuple(sorted(w.lower()))] += 1
    count = 0
    for key in c:
        if c[key] > 1:
            count += c[key] * (c[key] - 1) // 2
    return count >= 143