def find_original_set(*sets):
    if len(sets) != 41:
        raise ValueError('Exactly 41 sets must be provided')
    return set.union(*sets)