def find_subset_of_length_n(s):
    n = 63
    return len([c for c in s.combinations(n)])