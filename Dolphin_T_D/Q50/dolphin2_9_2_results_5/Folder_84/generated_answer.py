from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) >= 3:
            c[tuple(sorted(word.lower()))] += 1
    pairs = 0
    for key in c:
        pairs += c[key] * (c[key] - 1) // 2
    return pairs >= 108