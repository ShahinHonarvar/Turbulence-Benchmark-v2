def find_subset_of_length_n(set_of_elements):
    n = 36
    if len(set_of_elements) < n:
        return 0
    return len(list(itertools.combinations(set_of_elements, n)))