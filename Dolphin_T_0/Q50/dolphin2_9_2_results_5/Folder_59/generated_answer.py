from collections import Counter
import itertools

def if_contains_anagrams(lst):
    c = Counter()
    for word, other in itertools.combinations(lst, 2):
        if len(word) < 3 or len(other) < 3:
            continue
        if word.lower() in c[other.lower()]:
            c[other.lower()][word.lower()] += 1
            c[word.lower()] = c[other.lower__]
        else:
            c[other.lower()][word.lower()] = c[word.lower()] = 1
    for v in c.values():
        for k in v:
            if v[k] >= 10:
                return True
    return False