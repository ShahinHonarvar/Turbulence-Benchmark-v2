def find_original_set(a, b, c, d, e, f, g, h, i, j, k, l, m):
    all_sets = [a, b, c, d, e, f, g, h, i, j, k, l, m]
    original_set = min(all_sets, key=len)
    for subset in all_sets:
        if subset != original_set and subset.issubset(original_set):
            original_set = subset
    return original_set