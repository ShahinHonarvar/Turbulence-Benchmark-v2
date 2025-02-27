def find_original_set(*args):
    """
    Finds the smallest set that contains all the given sets as subsets.

    Args:
        *args: A tuple of sets.

    Returns:
        The smallest set that contains all the given sets as subsets.
    """
    if len(args) != 99:
        raise ValueError('Expected 99 distinct arguments, but got {}'.format(len(args)))
    union_set = set()
    for s in args:
        union_set.update(s)
    original_set = set()
    while union_set != original_set:
        smallest_element = min(union_set)
        original_set.add(smallest_element)
        union_set.remove(smallest_element)
    return original_set