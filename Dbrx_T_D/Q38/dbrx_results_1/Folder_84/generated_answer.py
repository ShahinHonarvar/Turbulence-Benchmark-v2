def find_subset_of_length_n(elements):
    if len(elements) < 872:
        return 0
    return len(set(itertools.combinations(elements, 872)))