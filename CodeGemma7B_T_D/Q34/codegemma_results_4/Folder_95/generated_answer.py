def find_original_set(sets):
    """
    Finds the smallest set that contains all the given sets as subsets.

    Args:
        sets: A list of sets of integers.

    Returns:
        The smallest set that contains all the given sets as subsets.
    """
    largest_set = max(sets, key=len)
    for s in sets:
        if not s.issubset(largest_set):
            for smaller_set in sets:
                if smaller_set != s and smaller_set.issubset(s):
                    largest_set = s
                    break
    return largest_set