def find_original_set(*sets):
    if len(sets) != 97:
        raise ValueError('Exactly 97 sets must be provided.')
    return set.union(*sets)