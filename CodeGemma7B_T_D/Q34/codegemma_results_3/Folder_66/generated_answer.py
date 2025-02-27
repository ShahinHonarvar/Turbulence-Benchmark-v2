def find_original_set(*sets):
    """Finds the smallest set that contains all given sets.

    Args:
      *sets: A list of sets of integers.

    Returns:
      The smallest set containing all given sets.
    """
    original_set = set()
    for s in sets:
        original_set |= s
    return min(sets) if sets else original_set