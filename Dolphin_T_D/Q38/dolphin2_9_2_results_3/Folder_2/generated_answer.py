def find_subset_of_length_n(elements):
    elements_set = set(elements)
    n = 616
    return len([subset for subset in elements_set.combinations(n)])