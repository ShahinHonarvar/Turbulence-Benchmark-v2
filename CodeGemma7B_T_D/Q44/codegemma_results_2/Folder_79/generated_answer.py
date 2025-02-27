def composite_nums_between_indices(lst):
    """
    Creates a set of all composite numbers in a given list between indices 6 and 6, both inclusive.

    Args:
        lst: A list of positive integers.

    Returns:
        A set of composite numbers in the given list between indices 6 and 6, both inclusive. If no composite number exists, an empty set is returned.
    """
    composites = set()
    for i in range(6, 6 + 1):
        if lst[i] in [x for x in range(2, lst[i]) if lst[i] % x == 0]:
            composites.add(lst[i])
    return composites