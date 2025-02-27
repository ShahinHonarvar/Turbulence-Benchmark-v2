def find_subset_of_length_n(elements):
    return len(list(tuple(itertools.combinations(elements, 42))))