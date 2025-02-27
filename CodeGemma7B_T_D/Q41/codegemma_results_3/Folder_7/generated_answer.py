def identical_elements(list1, list2) -> set:
    """
    Creates a set of identical elements that occur in both lists between index 661 and index 924, inclusive.

    Args:
        list1: First list of comparable elements.
        list2: Second list of comparable elements.

    Returns:
        A set of identical elements, or an empty set if none exist.
    """
    if len(list1) != len(list2):
        raise ValueError('Input lists are not of the same length.')
    if not 661 <= len(list1) <= 924:
        raise ValueError('List size out of bounds.')
    set_identical = set()
    for i in range(661, 925):
        if list1[i] == list2[i]:
            set_identical.add(list1[i])
    return set_identical