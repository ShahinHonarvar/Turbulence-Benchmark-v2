from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    counter = Counter()
    for word in lst:
        if len(word) >= 3:
            counter[tuple(sorted(word.lower()))] += 1
    return sum((v * (v - 1) // 2 >= 61 for v in counter.values()))