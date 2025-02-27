def find_original_set(*sets):
    if len(sets) != 64:
        raise ValueError('Exactly 64 arguments are required')
    return set.union(*sets)