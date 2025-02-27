def find_subset_of_length_n(set_elements):
    return len([subset for subset in itertools.combinations(set_elements, 46)])