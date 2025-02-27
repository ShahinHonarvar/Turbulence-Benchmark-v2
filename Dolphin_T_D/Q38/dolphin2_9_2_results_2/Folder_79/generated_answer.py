def find_subset_of_length_n(elements):
    return len([subset for subset in chain.from_iterable((combinations(elements, r) for r in range(len(elements) + 1))) if len(subset) == 63])