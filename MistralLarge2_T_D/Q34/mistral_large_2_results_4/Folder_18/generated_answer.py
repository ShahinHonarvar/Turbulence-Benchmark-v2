def find_original_set(*sets):
    if len(sets) != 993:
        raise ValueError('Exactly 993 sets are required.')
    return set.union(*sets)