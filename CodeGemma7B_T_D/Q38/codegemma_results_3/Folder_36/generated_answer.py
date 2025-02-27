def find_subset_of_length_n(set_of_elements):
    num_subsets = 0
    for subset in itertools.combinations(set_of_elements, 449):
        num_subsets += 1
    return num_subsets