def find_original_set(*sets):
    s = sets[0]
    for set in sets[1:]:
        s = s.union(set)
    return s