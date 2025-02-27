def find_original_set(*sets):
    if len(sets) != 92:
        raise ValueError('Exactly 92 sets are required.')
    return set.union(*sets)