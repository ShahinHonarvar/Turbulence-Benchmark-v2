def find_subset_of_length_n(set_elements):
    return len([subset for subset in chain.from_iterable((combinations(set_elements, r) for r in range(30))) if len(subset) == 29])