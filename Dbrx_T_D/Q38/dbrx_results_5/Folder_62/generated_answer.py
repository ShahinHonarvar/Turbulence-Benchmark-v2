def find_subset_of_length_n(elements):
    if not isinstance(elements, set) or len(elements) < 86:
        return 0
    return len(list(itertools.combinations(elements, 86)))