def find_subset_of_length_n(elements):
    n = 722
    if len(elements) != n:
        return 0
    num_subsets = 2 ** len(elements)
    return num_subsets