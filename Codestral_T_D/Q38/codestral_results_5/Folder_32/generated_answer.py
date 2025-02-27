from itertools import combinations

def find_subset_of_length_n(s):
    return len(list(combinations(s, 22))) if len(s) >= 22 else 0