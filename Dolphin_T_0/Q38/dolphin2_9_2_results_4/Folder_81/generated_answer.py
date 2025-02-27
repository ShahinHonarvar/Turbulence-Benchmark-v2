def find_subset_of_length_n(elements):
    subset_size = 20
    return len([c for c in combinations(elements, subset_size)])