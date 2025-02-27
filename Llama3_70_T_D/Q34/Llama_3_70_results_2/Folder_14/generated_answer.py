def find_original_set(a, b, c, d, e, f, g, h, i, j, k, l, m):
    original_set = a
    for s in [b, c, d, e, f, g, h, i, j, k, l, m]:
        original_set = original_set.union(s)
    return original_set