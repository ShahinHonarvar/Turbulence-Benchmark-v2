from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    pair_count = 0
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            c[tuple(sorted(word))] += 1
    for count in c.values():
        pair_count += count * (count - 1) // 2
    return pair_count >= 24