def find_subset_of_length_n(elements_set, n=96):
    if not isinstance(elements_set, set) or len(elements_set) < n:
        return 0
    return sum((1 for _ in itertools.combinations(elements_set, n)))