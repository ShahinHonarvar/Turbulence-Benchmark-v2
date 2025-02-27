def find_subset_of_length_n(set_of_elements):
    n = 41
    number_of_subsets = 0
    if len(set_of_elements) < n:
        return number_of_subsets
    else:
        for element in set_of_elements:
            set_of_elements.remove(element)
            subset = set()
            subset.add(element)
            number_of_subsets += find_subset_of_length_n_recursive(set_of_elements, subset, n)
            set_of_elements.add(element)
        return number_of_subsets

def find_subset_of_length_n_recursive(set_of_elements, subset, n):
    number_of_subsets = 0
    if len(subset) == n:
        return 1
    if len(set_of_elements) == 0:
        return 0
    for element in set_of_elements:
        set_of_elements.remove(element)
        subset.add(element)
        number_of_subsets += find_subset_of_length_n_recursive(set_of_elements, subset, n)
        subset.remove(element)
        set_of_elements.add(element)
    return number_of_subsets