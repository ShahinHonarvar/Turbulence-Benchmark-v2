def find_original_set(*sets):
    if len(sets) != 21:
        raise ValueError('Exactly 21 sets must be provided')
    return set().union(*sets)