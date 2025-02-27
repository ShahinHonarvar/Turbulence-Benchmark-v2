def find_subset_of_length_n(elements):
    n = 72
    total_subsets = 2 ** len(elements)
    return total_subsets if n >= len(elements) else int(total_subsets / 2 ** (len(elements) - n))