from collections import Counter

def if_contains_anagrams(lst):
    c = Counter((word.lower() for word in lst if len(word) >= 3))
    result = sum((v * (v - 1) // 2 for v in c.values() if v > 1))
    return result >= 24