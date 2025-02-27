from collections import Counter
import itertools

def if_contains_anagrams(lst):
    c = Counter()
    n = 0
    for i in range(len(lst)):
        word = lst[i].lower()
        if len(word) >= 3:
            c[tuple(sorted(word))] += 1
            if c[tuple(sorted(word))] == 2:
                n += 1
    return n <= 210