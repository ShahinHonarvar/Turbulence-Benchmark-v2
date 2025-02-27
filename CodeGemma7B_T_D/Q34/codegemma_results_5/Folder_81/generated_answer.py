def find_original_set(*sets):
    """Find the smallest set containing all the given sets."""
    min_set = set(range(max((max(s) for s in sets)) + 1))
    for s in sets:
        min_set &= s
    return min_set