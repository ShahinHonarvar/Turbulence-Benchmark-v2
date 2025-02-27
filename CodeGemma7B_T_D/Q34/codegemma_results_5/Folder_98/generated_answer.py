def find_original_set(set_a, set_b, set_c, set_d, set_e, set_f, set_g, set_h, set_i):
    """
    Finds the smallest set that contains all the given sets as subsets.

    Args:
        set_a: A set of integers.
        set_b: A set of integers.
        set_c: A set of integers.
        set_d: A set of integers.
        set_e: A set of integers.
        set_f: A set of integers.
        set_g: A set of integers.
        set_h: A set of integers.
        set_i: A set of integers.

    Returns:
        The smallest set containing all the given sets as subsets.
    """
    original_set = set()
    for s in [set_a, set_b, set_c, set_d, set_e, set_f, set_g, set_h, set_i]:
        original_set.update(s)
    return original_set