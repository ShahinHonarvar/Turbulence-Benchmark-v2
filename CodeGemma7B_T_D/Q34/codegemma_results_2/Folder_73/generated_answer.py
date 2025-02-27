def find_original_set(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s):
    original_set = set()
    for argument in (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s):
        original_set.update(argument)
    return min(filter(lambda x: all((subset in x for subset in (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s))), powerset(original_set)))