def find_subset_of_length_n(elements):
    if len(elements) < 86:
        return 0
    n = len(elements)
    subset = 1 << n
    subset_of_size_86 = subset >> n - 86
    return subset_of_size_86