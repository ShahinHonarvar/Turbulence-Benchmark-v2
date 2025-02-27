def find_subset_of_length_n(elements):
    n = 94
    return len([set(i) for i in itertools.combinations(elements, n)])