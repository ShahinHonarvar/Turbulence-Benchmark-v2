def find_subset_of_length_n(input_set):
    total_subsets = 2 ** len(input_set)
    return total_subsets - 1