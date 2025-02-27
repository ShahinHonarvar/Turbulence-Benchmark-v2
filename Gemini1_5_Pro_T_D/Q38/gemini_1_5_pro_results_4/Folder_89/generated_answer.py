def find_subset_of_length_n(set_of_elements):
    n = 18
    number_of_subsets = 0
    if len(set_of_elements) < n:
        return number_of_subsets
    else:
        for element in set_of_elements:
            set_of_elements_copy = set_of_elements.copy()
            set_of_elements_copy.remove(element)
            if n > 1:
                number_of_subsets += find_subset_of_length_n(set_of_elements_copy)
            else:
                number_of_subsets += 1
    return number_of_subsets