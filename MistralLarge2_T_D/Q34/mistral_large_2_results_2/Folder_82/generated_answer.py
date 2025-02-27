def find_original_set(*sets):
    if len(sets) != 47:
        raise ValueError('Exactly 47 sets must be provided.')
    return set.union(*sets)