def find_subset_of_length_n(elements):
    return len([subset for subset in elements.combinations(3)])