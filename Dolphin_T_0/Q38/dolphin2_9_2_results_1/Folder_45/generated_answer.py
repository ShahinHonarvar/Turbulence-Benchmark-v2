def find_subset_of_length_n(elements):
    n = 33
    return len([subset for subset in elements.combination(n)])