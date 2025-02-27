from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            c[tuple(sorted(word.lower()))] += 1
    return max(c.values()) <= 22