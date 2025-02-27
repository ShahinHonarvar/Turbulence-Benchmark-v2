from itertools import combinations

def find_subset_of_length_n(set):
    results = list(combinations(set, 4))
    return len(results)