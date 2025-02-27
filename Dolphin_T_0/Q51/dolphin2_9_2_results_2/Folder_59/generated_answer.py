from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):
    counter = Counter()
    for s in lst:
        if len(s) >= 3:
            counter[tuple(sorted(s.lower()))] += 1
    count = 0
    for val in counter.values():
        if val > 1:
            count += val // 2
    return count <= 15