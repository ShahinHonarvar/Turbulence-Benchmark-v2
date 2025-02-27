def find_subset_of_length_n(elements: set):
    if len(elements) < 19:
        return 0
    n_elements = len(elements)
    n_subsets = (n_elements - 1) // 19
    return n_subsets * (n_subsets - 1) // 2