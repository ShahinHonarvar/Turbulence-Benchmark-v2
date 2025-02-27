def find_original_set(*args):
    """
    Finds the smallest set that contains all the given sets as subsets.

    Args:
        *args: A variable-length list of sets.

    Returns:
        The smallest set that contains all the given sets as subsets.
    """
    original_sets = set()
    for s in args:
        original_sets.add(s)
    result = set()
    for s in original_sets:
        result.update(s)
    return result