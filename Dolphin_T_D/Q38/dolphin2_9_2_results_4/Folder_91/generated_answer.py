def find_subset_of_length_n(elements):
    n = 6
    return len([combo for combo in itertools.combinations(elements, n)])