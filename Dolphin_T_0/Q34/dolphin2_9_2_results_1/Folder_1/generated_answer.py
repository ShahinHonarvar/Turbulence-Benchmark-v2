def find_original_set(*sets):
    union = set()
    for s in sets:
        union = union.union(s)
    return union