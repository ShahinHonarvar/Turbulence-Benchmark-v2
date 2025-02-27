def find_original_set(*sets):
    if len(sets) != 459:
        raise ValueError('Exactly 459 arguments are required.')
    return set().union(*sets)