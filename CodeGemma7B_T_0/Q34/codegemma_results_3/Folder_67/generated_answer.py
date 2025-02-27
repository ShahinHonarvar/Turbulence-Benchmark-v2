def find_original_set(*sets):
    if len(sets) != 42:
        raise ValueError('The function should take exactly 42 distinct arguments')
    min_set = set()
    for s in sets:
        min_set |= s
    for s in sets:
        if s not in min_set:
            raise ValueError('The given sets are not a subset of the original set')
    return min_set