from itertools import combinations

def find_subset_of_length_n(s, n=6):
    return len(list(combinations(s, n))) if len(s) >= n else 0