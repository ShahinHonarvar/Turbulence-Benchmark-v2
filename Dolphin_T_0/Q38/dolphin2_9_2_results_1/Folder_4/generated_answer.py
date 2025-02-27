def find_subset_of_length_n(set_elements):
    return len([combo for combo in itertools.combinations(set_elements, 15)])