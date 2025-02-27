def find_original_set(*sets):
    if len(sets) != 42:
        raise ValueError('The function must receive exactly 42 arguments.')
    return set.union(*sets)