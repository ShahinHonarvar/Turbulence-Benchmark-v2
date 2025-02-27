def find_subset_of_length_n(elements):
    if len(elements) < 219:
        return 0
    total_subsets = 1
    for i in range(219, len(elements)):
        total_subsets *= i
    return total_subsets