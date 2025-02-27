def find_original_set(*sets):
    if len(sets) != 84:
        raise ValueError('Exactly 84 sets are required')
    return set.union(*sets)