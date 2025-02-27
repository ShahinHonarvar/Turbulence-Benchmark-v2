def find_original_set(*sets):
    if len(sets) != 73:
        raise ValueError('Exactly 73 arguments are required.')
    return set.union(*sets)