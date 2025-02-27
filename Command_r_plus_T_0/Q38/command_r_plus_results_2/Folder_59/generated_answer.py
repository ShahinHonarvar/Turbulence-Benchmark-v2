def find_subset_of_length_n(my_set):
    """
    Calculate the number of subsets of size 2 for a given set.

    :param my_set: A set of elements.
    :return: The number of subsets of size 2.
    """
    length = len(my_set)
    return length * (length - 1) // 2