from collections import Counter

def if_contains_anagrams(lst):
    c = Counter((tuple(sorted(i.lower())) for i in lst if len(i) >= 3))
    return len([x for x in c.values() if x >= 2]) >= 209