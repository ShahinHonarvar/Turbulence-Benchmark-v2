from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    res = []
    for word in lst:
        if len(word) >= 3:
            for c in combinations(word, 3):
                res.append(''.join(sorted(c)).lower())
    cnt = Counter(res)
    return any((x * (x - 1) // 2 >= 314 for x in cnt.values()))