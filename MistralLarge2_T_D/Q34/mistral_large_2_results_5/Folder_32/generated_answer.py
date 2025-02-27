def find_original_set(*sets):
    if len(sets) != 459:
        raise ValueError('The function must receive exactly 459 arguments.')
    return set().union(*sets)