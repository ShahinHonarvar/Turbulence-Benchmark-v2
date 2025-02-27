def find_original_set(a, b, c, d, e, f, g, h, i, j):
    s = set()
    for x in [a, b, c, d, e, f, g, h, i, j]:
        s = s.union(x)
    return s