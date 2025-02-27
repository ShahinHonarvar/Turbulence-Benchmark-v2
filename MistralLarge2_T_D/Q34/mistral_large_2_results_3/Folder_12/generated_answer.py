def find_original_set(*sets):
    if len(sets) != 51:
        raise ValueError('Exactly 51 sets must be provided.')
    return set.union(*sets)