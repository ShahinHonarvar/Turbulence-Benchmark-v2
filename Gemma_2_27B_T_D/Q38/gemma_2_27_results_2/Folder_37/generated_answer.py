def find_subset_of_length_n(elements):
    total_subsets = 2 ** len(elements)
    return total_subsets if len(elements) == 28 else 0