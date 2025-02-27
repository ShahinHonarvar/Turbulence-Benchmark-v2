from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    for word in lst:
        if len(word) >= 3:
            counter[tuple(sorted(word.lower()))] += 1
    pairs = sum((c * (c - 1) // 2 for c in counter.values() if c > 1))
    return pairs <= 74