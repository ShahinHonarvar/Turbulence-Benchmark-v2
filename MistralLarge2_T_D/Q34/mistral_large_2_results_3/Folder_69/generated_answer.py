def find_original_set(*sets):
    union_set = set()
    for s in sets:
        union_set.update(s)
    return union_set