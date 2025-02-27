def find_original_set(*sets):
    if len(sets) != 312:
        raise ValueError('Exactly 312 sets are required.')
    return set.union(*sets)