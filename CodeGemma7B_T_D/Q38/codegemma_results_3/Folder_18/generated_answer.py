from itertools import combinations

def find_subset_of_length_n(s):
    return len({frozenset(c) for c in combinations(s, 630)})