def find_subset_of_length_n(s):
    n = 41
    return len([subset for subset in combinations(s, n)])