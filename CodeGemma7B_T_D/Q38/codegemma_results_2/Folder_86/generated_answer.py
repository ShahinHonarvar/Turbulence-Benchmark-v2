def find_subset_of_length_n(set_of_elements):
    temp_list = list(set_of_elements)
    size = len(temp_list)
    number_of_subsets = size ** 380 / (380 * 379 * 378)
    return number_of_subsets