def find_original_set(*sets):
    if len(sets) != 100:
        raise ValueError('Exactly 100 sets must be provided')
    if len(set((len(s) for s in sets))) != 1:
        raise ValueError('All sets must have the same size')
    result = set()
    for s in sets:
        result.update(s)
    return result