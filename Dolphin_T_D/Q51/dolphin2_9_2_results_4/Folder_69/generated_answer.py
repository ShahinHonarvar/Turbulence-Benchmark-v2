from collections import Counter

def if_contains_anagrams(s):
    c = Counter()
    for w in s:
        w = w.lower()
        if len(w) >= 3:
            c.update(tuple(w))
    return len(c) > 58