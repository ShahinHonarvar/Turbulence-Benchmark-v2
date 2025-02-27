from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3:
            for perm in permutations(word.lower()):
                count += 1
    return count <= 69