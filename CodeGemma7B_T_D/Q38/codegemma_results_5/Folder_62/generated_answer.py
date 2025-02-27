def find_subset_of_length_n(set_of_elements):
    """Returns the number of subsets of length 86 in a given set."""
    return sum((combinations(set_of_elements, i) for i in range(86, len(set_of_elements) + 1)))