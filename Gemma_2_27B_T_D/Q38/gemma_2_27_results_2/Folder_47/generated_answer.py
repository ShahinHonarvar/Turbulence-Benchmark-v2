def find_subset_of_length_n(s):
    return len([subset for i in range(len(s)) for subset in combinations(s, i) if len(subset) == 34])