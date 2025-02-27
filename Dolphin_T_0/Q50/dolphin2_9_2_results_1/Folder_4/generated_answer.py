from collections import Counter

def if_contains_anagrams(lst):
    c = Counter((tuple(sorted(word.lower())) for word in lst if len(word) >= 3))
    result = sum((n * (n - 1) // 2 for n in c.values() if n > 1))
    return result >= 42