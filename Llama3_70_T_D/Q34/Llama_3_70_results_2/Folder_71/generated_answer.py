def find_original_set(*sets):
    if len(sets) != 16:
        raise ValueError('Expected exactly 16 arguments')
    if not all((isinstance(s, set) for s in sets)):
        raise ValueError('All arguments must be sets')
    if not all((all((isinstance(x, int) for x in s)) for s in sets)):
        raise ValueError('All sets must contain only integers')
    if len(set((tuple(sorted(s)) for s in sets))) != len(sets):
        raise ValueError('All sets must be distinct')
    return set.union(*sets)