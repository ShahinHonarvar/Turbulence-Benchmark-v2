def find_subset_of_length_n(set_of_elements):
    number_of_subsets = 0
    if len(set_of_elements) >= 54:
        number_of_subsets = 1
        for i in range(54):
            number_of_subsets *= len(set_of_elements) - i
            number_of_subsets //= i + 1
    return number_of_subsets