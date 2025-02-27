def find_subset_of_length_n(set_elements):
    n = 66
    return len([subset for i in range(len(set_elements)) for subset in itertools.combinations(set_elements, i) if len(subset) == n])