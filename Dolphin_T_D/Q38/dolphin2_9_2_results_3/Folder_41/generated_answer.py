def find_subset_of_length_n(set_elements):
    n = 84
    return len([subset for subset in itertools.combinations(set_elements, n)])