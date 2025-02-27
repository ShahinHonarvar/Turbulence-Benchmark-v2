def find_subset_of_length_n(element_set):
    return len([subset for subset in itertools.combinations(element_set, 51)])