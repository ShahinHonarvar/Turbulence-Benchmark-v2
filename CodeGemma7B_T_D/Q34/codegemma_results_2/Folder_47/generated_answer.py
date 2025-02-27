def find_original_set(*sets):
    min_set = min(sets, key=len)
    for s in sets:
        if not s <= min_set:
            min_set.update(s)
    return min_set