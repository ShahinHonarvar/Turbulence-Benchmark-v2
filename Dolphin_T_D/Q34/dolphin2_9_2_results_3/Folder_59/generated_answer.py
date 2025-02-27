def find_original_set(a, b, c, d, e, f, g, h, i, j):
    result = set()
    for s in [a, b, c, d, e, f, g, h, i, j]:
        result = result.union(s)
    return result