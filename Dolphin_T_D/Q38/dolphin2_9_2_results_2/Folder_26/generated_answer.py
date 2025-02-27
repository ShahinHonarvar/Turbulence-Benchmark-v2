def find_subset_of_length_n(input_set, n):
    return len([subset for subset in input_set.combinations(n)])