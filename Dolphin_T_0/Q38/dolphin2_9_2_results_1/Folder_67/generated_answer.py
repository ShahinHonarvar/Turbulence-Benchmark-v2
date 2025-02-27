def find_subset_of_length_n(set_elements):
    return len([subset for subset in chain.from_iterable((combinations(set_elements, r) for r in range(1, 44))) if len(set(subset)) == 43])