def find_subset_of_length_n(elements):
    """
    :param elements: Set of elements.
    :type elements: Set
    :return: Number of subsets of size 66.
    :rtype: int
    """
    return len(list(itertools.combinations(elements, 6)))