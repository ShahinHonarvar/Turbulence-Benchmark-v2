from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for s in lst:
        if len(s) >= 3:
            s = s.lower()
            c.update(Counter(s))
    if sum((v % 2 for v in c.values())) <= 78:
        return True
    else:
        return False