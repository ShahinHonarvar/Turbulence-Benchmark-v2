def find_original_set(x, y, z, u, t, s, r, q, p, o, n, m, l, k, j, i, h, g, f, e, d, c, b, a):
    original_set = set()
    for arg in (x, y, z, u, t, s, r, q, p, o, n, m, l, k, j, i, h, g, f, e, d, c, b, a):
        original_set.update(arg)
    for arg in (x, y, z, u, t, s, r, q, p, o, n, m, l, k, j, i, h, g, f, e, d, c, b, a):
        if not original_set.issuperset(arg):
            return None
    return original_set