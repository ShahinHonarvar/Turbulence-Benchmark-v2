from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for s in lst:
        if len(s) >= 3 and s.isalpha():
            c[Counter(s.lower())] += 1
    return max(c.values()) <= 78