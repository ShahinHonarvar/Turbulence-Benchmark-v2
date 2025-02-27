def find_original_set(*sets):
    """
    Returns the smallest set that contains all the given sets.
    """
    result = set()
    for s in sets:
        result = result | s
    return result