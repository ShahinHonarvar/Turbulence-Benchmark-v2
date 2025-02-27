def find_subset_of_length_n(elements):
    if len(elements) < 16:
        return 0
    return sum((1 for _ in itertools.combinations(elements, 16)))