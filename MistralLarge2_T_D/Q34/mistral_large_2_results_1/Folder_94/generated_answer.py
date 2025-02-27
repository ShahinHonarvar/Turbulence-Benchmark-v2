def find_original_set(*sets):
    if len(sets) != 69:
        raise ValueError('Exactly 69 sets are required')
    return set.union(*sets)