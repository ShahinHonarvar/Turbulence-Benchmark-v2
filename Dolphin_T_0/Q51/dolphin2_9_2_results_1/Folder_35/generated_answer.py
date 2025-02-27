import string
    from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    for word in lst:
        if len(word) >= 3:
            counter[tuple(sorted(word.lower()))] += 1
    count = 0
    for c in counter.values():
        count += c * (c - 1) // 2
    return count <= 210