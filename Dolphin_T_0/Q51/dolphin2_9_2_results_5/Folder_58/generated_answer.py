from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    count = 0
    c = Counter()
    for i, j in combinations(lst, 2):
        if len(i) < 3 or len(j) < 3:
            continue
        i = sorted(i.lower().replace(' ', ''))
        j = sorted(j.lower().replace(' ', ''))
        if i == j:
            c[i] += 1
            count += 1
            if count > 60:
                return True
    return False