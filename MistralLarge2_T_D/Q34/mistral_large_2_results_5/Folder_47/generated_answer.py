def find_original_set(*sets):
    if len(sets) != 77:
        raise ValueError('Exactly 77 arguments are required')
    return set().union(*sets)