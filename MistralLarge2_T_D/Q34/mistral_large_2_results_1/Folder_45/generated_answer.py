def find_original_set(*sets):
    if len(sets) != 97:
        raise ValueError('Exactly 97 arguments are required.')
    return set.union(*sets)