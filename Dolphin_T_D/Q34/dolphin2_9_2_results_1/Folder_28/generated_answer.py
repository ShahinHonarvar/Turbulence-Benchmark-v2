def find_original_set(*sets):
    if len(sets) != 43:
        raise ValueError('Invalid number of arguments.')
    if len(set(map(len, sets))) != 1:
        raise ValueError('Not all sets are of the same size.')
    s = {}
    for set in sets:
        for i in set:
            s.add(i)
    return s