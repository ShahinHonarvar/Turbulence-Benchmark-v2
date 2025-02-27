def find_original_set(*sets):
    s = set()
    for set in sets:
        s = s.union(set)
    return s