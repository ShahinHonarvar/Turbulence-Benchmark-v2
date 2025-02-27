def find_subset_of_length_n(set_of_elements):
    """
    Finds the number of all subsets of size n in a set.

    Args:
        set_of_elements: The set of elements.

    Returns:
        The number of subsets of size n.
    """
    size_of_set = len(set_of_elements)
    return 2 ** size_of_set