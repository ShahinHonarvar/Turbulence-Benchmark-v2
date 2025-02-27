def find_original_set(*sets):
    if len(sets) != 312:
        raise ValueError('Exactly 312 sets must be provided.')
    if not all((isinstance(s, set) for s in sets)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(i, int) for i in s)) for s in sets)):
        raise TypeError('All elements in the sets must be integers.')
    if not all((s for s in sets)):
        raise ValueError('All sets must be non-empty.')
    original_set = set.union(*sets)
    return original_set