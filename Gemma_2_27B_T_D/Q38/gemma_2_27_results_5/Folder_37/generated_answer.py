def find_subset_of_length_n(s):
    n = 28
    return len([subset for i in range(len(s)) for subset in combinations(s, i + 1) if len(subset) == n])