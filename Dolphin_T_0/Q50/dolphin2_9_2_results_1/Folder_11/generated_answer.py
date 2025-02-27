from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) >= 3:
            c[tuple(sorted(word.lower()))] += 1
    count = 0
    for key, value in c.items():
        if value >= 2:
            count += value * (value - 1) // 2
    return count >= 28