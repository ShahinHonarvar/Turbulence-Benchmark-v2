def find_subset_of_length_n(set_of_elements):
    return len({x for x in set_combinations(set_of_elements, 3)})