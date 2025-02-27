def find_original_set(*sets):
    if len(sets) != 746:
        raise ValueError('Exactly 746 sets are required')
    original_set = set().union(*sets)
    return original_set