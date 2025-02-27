def find_subset_of_length_n(set_of_elements):
    return len([subset for i in range(len(set_of_elements) + 1) for subset in combinations(set_of_elements, i) if len(subset) == 722])