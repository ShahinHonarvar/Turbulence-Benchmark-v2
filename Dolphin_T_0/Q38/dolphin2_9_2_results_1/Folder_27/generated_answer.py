def find_subset_of_length_n(set_elements):
    return len([s for s in chain.from_iterable((combinations(set_elements, r) for r in range(len(set_elements) + 1))) if len(s) == 56])