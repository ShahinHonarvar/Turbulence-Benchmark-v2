def find_original_set(*sets):
    original_set = sets[0]
    for s in sets:
        original_set |= s
    return original_set