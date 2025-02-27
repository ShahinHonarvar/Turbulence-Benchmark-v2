def find_original_set(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q):
    result = set(range(1, 99))
    for s in [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q]:
        result &= s
    return result