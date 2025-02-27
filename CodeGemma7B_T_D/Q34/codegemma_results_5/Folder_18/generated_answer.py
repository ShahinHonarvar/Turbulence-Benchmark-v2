def find_original_set(sets):
    min_set = min(sets, key=len)
    for s in sets:
        if not min_set.issuperset(s):
            min_set = min(min_set, s, key=len)
    return min_set