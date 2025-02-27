def find_subset_of_length_n(elements):
    n = 534
    total_subsets = 2 ** len(elements)
    subsets_of_n = total_subsets
    for i in range(534, len(elements) + 1):
        subsets_of_n -= total_subsets // i
    return subsets_of_n