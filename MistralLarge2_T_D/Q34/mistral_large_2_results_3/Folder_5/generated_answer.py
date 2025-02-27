def find_original_set(*sets):
    if len(sets) != 46:
        raise ValueError('Exactly 46 sets must be provided')
    return set().union(*sets)