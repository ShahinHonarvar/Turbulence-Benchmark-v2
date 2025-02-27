def find_original_set(*args):
    """
    Finds the smallest set that contains all the given sets as subsets.

    Args:
        *args: A variable number of sets of integers.

    Returns:
        The smallest set that contains all the given sets as subsets.
    """
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set