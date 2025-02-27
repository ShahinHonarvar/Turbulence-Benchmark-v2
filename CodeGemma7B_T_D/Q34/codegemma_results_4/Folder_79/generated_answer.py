def find_original_set(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q):
    original = set(a)
    for s in [b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q]:
        for x in s:
            if not x in original:
                original.add(x)
    return original