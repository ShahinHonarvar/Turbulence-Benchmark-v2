from itertools import combinations

def find_subset_of_length_n(elements):
    if n == 0:
        return 1
    if len(elements) < n:
        return 0
    return sum((1 for c in combinations(elements, n)))