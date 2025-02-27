def find_original_set(*sets):
    original_set = sets[0]
    for i in range(1, 40):
        original_set.update(sets[i])
    return original_set