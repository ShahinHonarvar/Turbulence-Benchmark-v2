from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            c[tuple(sorted(word))] += 1
    pairs = 0
    for letter in c.values():
        pairs += letter * (letter - 1) // 2
    return pairs <= 257