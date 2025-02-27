def find_subset_of_length_n(my_set):
    total_elements = len(my_set)
    num_subsets = total_elements * (total_elements - 1) * (total_elements - 2) / 6
    return num_subsets