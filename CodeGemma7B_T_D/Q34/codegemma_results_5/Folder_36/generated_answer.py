def find_original_set(*sets):
    """
    Return the smallest set containing all of the given sets.
    """
    min_set = min(sets, key=len)
    for s in sets:
        if not s.issubset(min_set):
            min_set.update(s)
    return min_set