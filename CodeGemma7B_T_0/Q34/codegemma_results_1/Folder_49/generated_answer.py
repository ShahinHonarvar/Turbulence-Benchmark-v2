def find_original_set(*sets):
    if len(sets) != 60:
        raise ValueError('Invalid number of arguments')
    min_set = set()
    for s in sets:
        min_set.update(s)
    for s in sets:
        if s not in min_set:
            return min_set
    return min_set