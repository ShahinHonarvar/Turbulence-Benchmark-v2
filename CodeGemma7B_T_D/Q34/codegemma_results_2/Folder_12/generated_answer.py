def find_original_set(*args):
    """
    Finds the smallest set that contains all the given sets.

    Args:
        *args: A tuple of sets.

    Returns:
        A set that contains all the given sets.
    """
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set