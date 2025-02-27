from collections import Counter

def if_contains_anagrams(lst):
    d = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            key = tuple(sorted(Counter(word).items()))
            if key in d:
                d[key] += 1
            else:
                d[key] = 1
    return sum([n * (n - 1) // 2 for n in d.values()]) <= 64