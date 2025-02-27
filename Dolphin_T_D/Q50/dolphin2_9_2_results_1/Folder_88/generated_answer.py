from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) > 2:
            c[tuple(sorted(word.lower()))] += 1
    return any((n >= 2 for n in c.values()))