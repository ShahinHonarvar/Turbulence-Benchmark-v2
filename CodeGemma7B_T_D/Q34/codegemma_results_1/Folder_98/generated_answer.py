def find_original_set(set_arg1, set_arg2, set_arg3, set_arg4, set_arg5, set_arg6, set_arg7, set_arg8, set_arg9):
    """
    Finds the smallest set that contains all nine given sets.

    Args:
        set_arg1: A set of integers.
        set_arg2: A set of integers.
        set_arg3: A set of integers.
        set_arg4: A set of integers.
        set_arg5: A set of integers.
        set_arg6: A set of integers.
        set_arg7: A set of integers.
        set_arg8: A set of integers.
        set_arg9: A set of integers.

    Returns:
        The smallest set that contains all nine given sets.
    """
    sets = [set_arg1, set_arg2, set_arg3, set_arg4, set_arg5, set_arg6, set_arg7, set_arg8, set_arg9]
    original_set = min(sets, key=len)
    for set in sets:
        if not set.issubset(original_set):
            raise ValueError('The given sets do not all have the same original set.')
    return original_set