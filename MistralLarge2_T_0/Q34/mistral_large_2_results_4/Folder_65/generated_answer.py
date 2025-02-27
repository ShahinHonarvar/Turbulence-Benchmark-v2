def find_original_set(*sets):
    if len(sets) != 80:
        raise ValueError('Exactly 80 sets must be provided.')
    return set.union(*sets)