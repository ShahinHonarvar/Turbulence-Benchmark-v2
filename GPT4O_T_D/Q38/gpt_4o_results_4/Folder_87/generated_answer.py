from itertools import combinations

def find_subset_of_length_n(s):
    return len(list(combinations(s, 96))) if len(s) >= 96 else 0