from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) >= 3:
            c[tuple(sorted(word.lower()))] += 1
    count = sum((v(v - 1) // 2 for v in c.values() if v > 1))
    return count >= 93