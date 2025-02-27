from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    ana_pairs = 0
    for word in lst:
        if len(word) >= 3:
            c[tuple(sorted(word.lower()))] += 1
    for count in c.values():
        if count > 1:
            ana_pairs += count * (count - 1) // 2
    return ana_pairs >= 68