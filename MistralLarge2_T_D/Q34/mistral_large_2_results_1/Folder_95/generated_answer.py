def find_original_set(*sets):
    if len(sets) != 88:
        raise ValueError('Exactly 88 distinct arguments are required.')
    return set.union(*sets)