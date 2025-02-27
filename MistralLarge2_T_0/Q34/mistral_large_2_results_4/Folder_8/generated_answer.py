def find_original_set(*sets):
    if len(sets) != 45:
        raise ValueError('Exactly 45 sets are required.')
    return set.union(*sets)