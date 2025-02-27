def find_original_set(sets):
    min_set = set()
    for s in sets:
        min_set.update(s)
    return min_set