def find_subset_of_length_n(s):
    n = 380
    return len([subset for i in range(len(s)) for subset in combinations(s, i) if len(subset) == n])