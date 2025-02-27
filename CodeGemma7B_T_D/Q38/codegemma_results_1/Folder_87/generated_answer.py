def find_subset_of_length_n(set_of_elements):
    num_subsets = 2 ** len(set_of_elements)
    num_subsets_of_length_96 = num_subsets - 2 ** (len(set_of_elements) - 96)
    return num_subsets_of_length_96