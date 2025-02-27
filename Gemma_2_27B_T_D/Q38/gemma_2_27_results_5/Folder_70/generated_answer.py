def find_subset_of_length_n(elements):
    n = len(elements)
    total_subsets = 1 << n
    return total_subsets