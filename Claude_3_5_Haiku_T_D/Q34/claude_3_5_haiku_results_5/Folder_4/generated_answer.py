def find_original_set(*sets):
    if len(sets) != 40:
        raise ValueError('Function requires exactly 40 distinct sets')
    return set().union(*sets)