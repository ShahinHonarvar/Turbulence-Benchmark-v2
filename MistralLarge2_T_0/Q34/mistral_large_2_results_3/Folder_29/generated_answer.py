def find_original_set(*sets):
    if len(sets) != 94:
        raise ValueError('Exactly 94 sets must be provided.')
    return set.union(*sets)