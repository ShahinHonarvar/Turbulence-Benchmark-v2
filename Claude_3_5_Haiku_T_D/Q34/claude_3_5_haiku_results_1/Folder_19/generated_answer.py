def find_original_set(*sets):
    if len(sets) != 23:
        raise ValueError('Function must be called with exactly 23 sets')
    return set().union(*sets)