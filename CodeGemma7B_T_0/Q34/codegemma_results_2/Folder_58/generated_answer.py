def find_original_set(*args):
    """
    Finds the smallest set that contains all the given sets as subsets.

    Args:
        *args: A tuple of sets.

    Returns:
        The smallest set that contains all the given sets as subsets.
    """
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set