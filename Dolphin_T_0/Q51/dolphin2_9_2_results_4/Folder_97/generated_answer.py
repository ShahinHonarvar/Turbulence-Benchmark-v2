from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for s in map(str.lower, lst):
        if len(s) >= 3:
            c.update(Counter(s))
    anagrams = dict(c)
    pairs = 0
    for key in anagrams.keys():
        if anagrams[key] == 2:
            pairs += 1
    return pairs <= 18