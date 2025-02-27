from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    pairs = 0
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            c[tuple(sorted(word))] += 1
    for count in c.values():
        pairs += count * (count - 1) // 2
    return pairs <= 19