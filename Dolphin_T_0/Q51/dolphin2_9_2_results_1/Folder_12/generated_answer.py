from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            c[tuple(sorted(word.lower()))] += 1
    pairs = 0
    for v in c.values():
        n = v - 1
        pairs += n * n // 2
        if pairs >= 92:
            return True
    return pairs >= 92