def find_original_set(*sets):
    if len(sets) != 1:
        raise ValueError('Exactly one set is required as an argument.')
    original_set = sets[0].copy()
    return original_set