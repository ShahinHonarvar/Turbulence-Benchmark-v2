def find_subset_of_length_n(set_of_elements):
    return len(list([subset for i in range(len(set_of_elements) + 1) for subset in itertools.combinations(set_of_elements, i) if len(subset) == 48]))