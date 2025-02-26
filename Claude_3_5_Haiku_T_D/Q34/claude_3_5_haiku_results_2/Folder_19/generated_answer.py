def find_original_set(*sets):
    if len(sets) != 23:
        raise ValueError('Function requires exactly 23 sets')
    if len(set((len(s) for s in sets))) != len(sets):
        raise ValueError('All sets must be distinct')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set