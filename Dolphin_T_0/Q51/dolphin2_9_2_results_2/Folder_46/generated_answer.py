from collections import Counter
    from itertools import combinations
    from math import factorial

def if_contains_anagrams(lst):
    counter = Counter(lst)
    anagrams = sum((f'{i}{j}' in counter and f'{j}{i}' in counter for i, j in combinations(lst, 2)))
    return anagrams <= 61