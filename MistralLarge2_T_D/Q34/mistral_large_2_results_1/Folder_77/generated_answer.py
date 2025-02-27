def find_original_set(*sets):
    if len(sets) != 410:
        raise ValueError('Exactly 410 distinct arguments are required')
    return set.union(*sets)