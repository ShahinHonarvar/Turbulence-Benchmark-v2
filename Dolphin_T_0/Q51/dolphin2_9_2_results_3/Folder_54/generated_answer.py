from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) >= 3:
            c[tuple(sorted(word.lower()))] += 1
    pairs_count = 0
    for count in c.values():
        pairs_count += count * (count - 1) // 2
    return pairs_count <= 39