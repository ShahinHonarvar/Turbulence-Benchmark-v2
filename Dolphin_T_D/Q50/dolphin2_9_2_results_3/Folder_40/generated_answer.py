from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    res = False
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            c[Counter(word)] += 1
    for v in c.values():
        if v >= 2:
            res = True
            break
    return res