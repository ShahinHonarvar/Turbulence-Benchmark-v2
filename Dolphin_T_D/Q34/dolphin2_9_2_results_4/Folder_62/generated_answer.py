def find_original_set(*sets):
    unified_set = set()
    for s in sets:
        unified_set = unified_set.union(s)
    return unified_set