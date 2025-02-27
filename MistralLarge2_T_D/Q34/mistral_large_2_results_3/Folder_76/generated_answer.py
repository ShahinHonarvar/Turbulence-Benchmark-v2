def find_original_set(*sets):
    if len(sets) != 247:
        raise ValueError('Exactly 247 distinct arguments are required.')
    return set.union(*sets)