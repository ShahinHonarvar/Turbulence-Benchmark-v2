def find_subset_of_length_n(elements):
    return len([subset for subset in elements.copy() if len(subset) == 89])