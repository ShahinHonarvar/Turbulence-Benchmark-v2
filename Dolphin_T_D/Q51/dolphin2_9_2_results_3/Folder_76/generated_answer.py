from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) >= 3:
            low_word = word.lower()
            c[tuple(sorted(low_word))] += 1
    pairs = 0
    for v in c.values():
        pairs += v * (v - 1) // 2
    return pairs <= 91