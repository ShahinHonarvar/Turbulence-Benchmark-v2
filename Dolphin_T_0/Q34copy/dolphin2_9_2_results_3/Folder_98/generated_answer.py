def find_original_set(a, b, c, d, e, f, g, h, i):
    sets = [a, b, c, d, e, f, g, h, i]
    original_set = set()
    for s in sets:
        original_set = original_set.union(s)
    return original_set