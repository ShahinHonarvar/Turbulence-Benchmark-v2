def find_original_set(*sets):
    if len(sets) != 23:
        raise ValueError('Exactly 23 sets are required.')
    return set.union(*sets)