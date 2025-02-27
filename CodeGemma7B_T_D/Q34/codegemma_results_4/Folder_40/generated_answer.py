def find_original_set(first_set, second_set):
    """
    This function finds the smallest set that contains the two input sets.

    Args:
        first_set: The first set of integers.
        second_set: The second set of integers.

    Returns:
        The smallest set that contains the two input sets.
    """
    original_set = set()
    original_set.update(first_set)
    original_set.update(second_set)
    return original_set