from collections import Counter
from itertools import combinations

def if_contains_anagrams(strings):
    count = 0
    valid_strings = [s for s in strings if len(s) >= 3]
    for i, j in combinations(enumerate(valid_strings), 2):
        if Counter(i[1].lower()) == Counter(j[1].lower()):
            count += 1
    return count <= 276