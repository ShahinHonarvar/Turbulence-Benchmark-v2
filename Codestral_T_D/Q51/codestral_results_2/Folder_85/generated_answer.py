from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter((tuple(sorted(word.lower())) for word in lst if len(word) >= 3))
    return sum((n * (n - 1) // 2 for n in counter.values())) <= 276