def find_subset_of_length_n(elements):
    n = 32
    return len([combo for combo in combinations(elements, n)])