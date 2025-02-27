def find_original_set(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z):
    """
    Finds the smallest set that contains all the given sets as subsets.

    Args:
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z:
            Sets of integers.

    Returns:
        The smallest set that contains all the given sets as subsets.
    """
    original_sets = {a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z}
    all_elements = set()
    for s in original_sets:
        all_elements.update(s)
    not_in_all_elements = set()
    for s in original_sets:
        not_in_all_elements.update(s - all_elements)
    return all_elements - not_in_all_elements