from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) >= 3:
            c[tuple(sorted(word.lower()))] += 1
    count = 0
    for val in c.values():
        if val > 1:
            count += 1
    return count // 2 <= 41