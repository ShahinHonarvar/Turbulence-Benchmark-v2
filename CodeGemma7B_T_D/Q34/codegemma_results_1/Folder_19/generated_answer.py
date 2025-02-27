def find_original_set(*sets):
    if len(sets) != 23:
        raise ValueError('Number of sets must be 23.')
    return min(sets, key=len)