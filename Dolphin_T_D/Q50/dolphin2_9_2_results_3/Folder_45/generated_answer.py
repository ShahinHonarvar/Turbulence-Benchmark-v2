from collections import Counter

def if_contains_anagrams(lst):
    c = Counter((tuple(sorted((s.lower() for s in wdgr))) for wdgr in lst if len(wdgr) >= 3))
    return any((v >= 277 for v in c.values()))