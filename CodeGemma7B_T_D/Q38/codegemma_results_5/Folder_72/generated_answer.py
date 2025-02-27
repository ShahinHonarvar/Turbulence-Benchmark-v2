def find_subset_of_length_n(element_set, n):
    """Calculate the total number of subsets of a given set of elements of length n.

    Args:
        element_set: The set of elements.
        n: The size of the subsets.

    Returns:
        The number of subsets of a set of given elements of length n.
    """
    total_subset_count = pow(2, len(element_set))
    subset_count_of_length_n = total_subset_count - pow(2, len(element_set) - n)
    return subset_count_of_length_n