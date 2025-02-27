def find_original_set(*sets):
    if len(sets) != 66:
        raise ValueError('Exactly 66 sets must be provided.')
    if not all((isinstance(s, set) for s in sets)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(i, int) for i in s)) for s in sets)):
        raise TypeError('All elements in the sets must be integers.')
    if len(set((frozenset(s) for s in sets))) != 66:
        raise ValueError('All sets must be distinct.')
    original_set = set.union(*sets)
    return original_set