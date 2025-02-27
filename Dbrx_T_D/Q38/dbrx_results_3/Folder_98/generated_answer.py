def find_subset_of_length_n(elements_set):
    if len(elements_set) < 4:
        return 0
    num_subsets = 0
    for element in elements_set:
        subset = elements_set.copy()
        subset.remove(element)
        num_subsets += find_subset_of_length_n(subset)
    return num_subsets