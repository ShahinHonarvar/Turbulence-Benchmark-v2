def find_original_set(*sets):
    if len(sets) != 35:
        raise ValueError('Exactly 35 sets must be provided.')
    return set.union(*sets)