def find_original_set(*sets):
    if len(sets) != 990:
        raise ValueError('Exactly 990 sets are required.')
    return set.union(*sets)