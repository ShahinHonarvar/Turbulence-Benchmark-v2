def find_original_set(*sets):
    if len(sets) != 733:
        raise ValueError('Function requires exactly 733 distinct sets')
    return set.union(*sets)