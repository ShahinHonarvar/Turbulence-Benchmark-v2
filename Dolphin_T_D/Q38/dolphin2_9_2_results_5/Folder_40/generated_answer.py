def find_subset_of_length_n(elements):
    return len([combo for combo in itertools.combinations(elements, 7)])