from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            key = ''.join(sorted(s))
            d[key].append(s)
    for key in d:
        if len(d[key]) > 26:
            return False
    return True