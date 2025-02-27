def find_original_set(*sets):
    """
    Finds the smallest set that contains each of the given sets as a subset.

    Args:
        *sets: Zero or more sets of integers.

    Returns:
        The smallest set that contains each of the given sets as a subset.
    """
    result_set = set()
    for s in sets:
        result_set.update(s)
    return min(sets, key=len)