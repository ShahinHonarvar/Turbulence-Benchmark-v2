def find_subset_of_length_n(elements):
    total_subsets = 2 ** len(elements)
    subsets_of_length_n = total_subsets - (total_subsets >> 73)
    return subsets_of_length_n