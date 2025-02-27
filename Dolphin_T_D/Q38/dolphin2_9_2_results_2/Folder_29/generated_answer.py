def find_subset_of_length_n(elements):
    return len([subset for i in range(len(elements) + 1) for subset in combinations(elements, i) if len(subset) == 19])