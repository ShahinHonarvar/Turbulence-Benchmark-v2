from collections import Counter

def if_contains_anagrams(lst):
    c = Counter((word.lower() for word in lst if len(word) >= 3))
    return any((value >= 2 for value in c.values()))