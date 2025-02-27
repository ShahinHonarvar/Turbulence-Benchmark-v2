def find_subset_of_length_n(elements):
    n = 28
    return len([subset for subset in combinations(elements, n)])