def find_original_set(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t):
    all_sets = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t]
    original_set = min(all_sets, key=len)
    for subset in all_sets:
        if subset not in original_set:
            original_set.update(subset)
    return original_set