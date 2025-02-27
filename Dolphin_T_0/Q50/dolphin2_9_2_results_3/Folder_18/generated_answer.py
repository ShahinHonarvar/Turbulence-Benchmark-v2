from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) >= 3:
            c[tuple(sorted(word.lower()))] += 1
    count = sum((x * (x - 1) // 2 for x in c.values() if x >= 2))
    return count >= 106