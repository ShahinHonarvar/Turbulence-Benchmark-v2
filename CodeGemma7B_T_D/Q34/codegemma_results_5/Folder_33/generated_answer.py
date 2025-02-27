def find_original_set(*sets):
    min_set = set(range(1, 264))
    for s in sets:
        min_set &= s
    return min_set