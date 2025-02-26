def find_original_set(*sets):
    if len(sets) != 5:
        raise ValueError('Function requires exactly 5 sets')
    if len(set((len(s) for s in sets))) != len(sets):
        raise ValueError('All input sets must be distinct')
    return set().union(*sets)