def find_subset_of_length_n(elements):
    n = 801
    total_subsets = 2 ** len(elements)
    subsets_of_length_n = total_subsets // 2 ** (len(elements) - n) - total_subsets // 2 ** (len(elements) - (n + 1))
    return subsets_of_length_n