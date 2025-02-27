def find_original_set(*sets):
    if len(sets) != 685:
        raise ValueError('Exactly 685 sets must be provided')
    return set.union(*sets)