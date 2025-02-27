from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    count = 0
    pairs = 0
    for word in lst:
        if len(word) >= 3:
            count += 1
            pairs += sum(combinations(Counter(word.lower()), 2))
    return count <= 79