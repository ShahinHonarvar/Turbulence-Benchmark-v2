from itertools import combinations

def find_subset_of_length_n(s):
    return len(list(combinations(s, 36))) if len(s) >= 36 else 0