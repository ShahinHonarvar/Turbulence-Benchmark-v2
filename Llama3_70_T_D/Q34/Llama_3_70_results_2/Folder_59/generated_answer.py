def find_original_set(a, b, c, d, e, f, g, h, i, j):
    original_set = a
    for set in [b, c, d, e, f, g, h, i, j]:
        original_set = original_set.union(set)
    return original_set