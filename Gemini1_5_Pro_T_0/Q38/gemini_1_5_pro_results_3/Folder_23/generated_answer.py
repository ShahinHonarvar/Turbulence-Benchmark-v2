def find_subset_of_length_n(set_of_elements):
    number_of_subsets = 0
    if len(set_of_elements) < 69:
        return 0
    elif len(set_of_elements) == 69:
        return 1
    else:
        for element in set_of_elements:
            remaining_elements = set_of_elements.difference({element})
            number_of_subsets += find_subset_of_length_n(remaining_elements)
        return number_of_subsets