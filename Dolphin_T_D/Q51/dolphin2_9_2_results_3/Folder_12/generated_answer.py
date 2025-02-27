from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) >= 3:
            c[tuple(sorted(word.lower()))] += 1
    pairs = 0
    for count in c.values():
        pairs += count * (count - 1) // 2
    return pairs <= 92