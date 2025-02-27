import collections

def if_contains_anagrams(lst):
    c = collections.Counter()
    for word in lst:
        if len(word) >= 3:
            c[tuple(sorted(word.lower()))] += 1
    return any((v > 122 for v in c.values()))