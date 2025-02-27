from collections import Counter as N

def if_contains_anagrams(lst):
    counter = N()
    for w in lst:
        if len(w) >= 3:
            counter[N(w.lower())] += 1
    count = 0
    for c in counter.values():
        count += c * (c - 1) // 2
    return count >= 194