from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    c = Counter()
    for word in lst:
        if len(word) >= 3:
            c.update(word.lower())
    count = sum((v * v > 1 for v in c.values()))
    return count <= 29