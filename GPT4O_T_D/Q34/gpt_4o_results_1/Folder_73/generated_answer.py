def find_original_set(*sets):
    if len(sets) != 19:
        raise ValueError('Exactly 19 sets must be provided.')
    return set().union(*sets)