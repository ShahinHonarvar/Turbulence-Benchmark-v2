def find_original_set(*sets):
    if len(sets) != 845:
        raise ValueError('Exactly 845 arguments required.')
    return set.union(*sets)