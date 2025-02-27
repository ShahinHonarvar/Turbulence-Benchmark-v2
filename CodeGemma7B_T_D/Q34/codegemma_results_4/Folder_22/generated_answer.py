def find_original_set(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z):
    sets = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
    original_set = min(sets, key=len)
    for a_set in sets:
        if a_set != original_set and (not original_set.issuperset(a_set)):
            return None
    return original_set