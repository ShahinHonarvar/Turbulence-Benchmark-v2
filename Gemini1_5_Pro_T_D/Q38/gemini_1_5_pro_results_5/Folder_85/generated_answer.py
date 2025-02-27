def find_subset_of_length_n(set_of_elements):
    n = 23
    number_of_subsets = 0
    if len(set_of_elements) < n:
        return number_of_subsets
    else:
        for element in set_of_elements:
            set_of_elements.remove(element)
            subset = {element}
            number_of_subsets += find_subset_of_length_n(set_of_elements.copy(), n - 1, subset)
        return number_of_subsets