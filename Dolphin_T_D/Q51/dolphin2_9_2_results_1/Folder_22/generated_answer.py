from collections import Counter

def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if len(s) >= 3]
    counter = Counter(lst)
    pairs = sum((v * (v - 1) // 2 for v in counter.values() if v > 1))
    return pairs <= 14