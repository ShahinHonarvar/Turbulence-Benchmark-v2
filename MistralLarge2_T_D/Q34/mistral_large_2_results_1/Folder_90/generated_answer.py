def find_original_set(*sets):
    if len(sets) != 985:
        raise ValueError('Exactly 985 sets must be provided.')
    return set.union(*sets)