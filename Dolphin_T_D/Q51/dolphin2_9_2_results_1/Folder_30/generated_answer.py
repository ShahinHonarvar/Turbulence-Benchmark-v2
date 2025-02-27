import collections

def if_contains_anagrams(lst):
    c = collections.Counter()
    d = {}
    for i in lst:
        i = i.lower()
        if len(i) >= 3:
            k = c.copy()
            for v in i:
                k[v] += 1
            if str(k) not in d:
                d[str(k)] = i
            else:
                return True
    return len(d) <= 28