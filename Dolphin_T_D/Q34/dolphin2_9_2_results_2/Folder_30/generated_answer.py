def find_original_set(*sets):
    union_all = sets[0]
    for a_set in sets[1:]:
        union_all = union_all.union(a_set)
    return union_all