def find_original_set(*sets):
    if len(sets) != 67:
        raise ValueError('Exactly 67 sets are required.')
    return set.union(*sets)