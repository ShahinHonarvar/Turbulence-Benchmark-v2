from collections import defaultdict

def if_contains_anagrams(strings):
    d = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            d[key].append(s)
    for key in d:
        if len(d[key]) >= 2:
            pairs = len(d[key]) * (len(d[key]) - 1) // 2
            if pairs >= 24:
                return True
    return False