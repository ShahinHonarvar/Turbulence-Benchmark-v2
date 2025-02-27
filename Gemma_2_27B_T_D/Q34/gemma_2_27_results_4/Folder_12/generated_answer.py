def find_original_set(*sets):
    original_set = sets[0]
    for i in range(1, 51):
        original_set = original_set.union(sets[i])
    return original_set