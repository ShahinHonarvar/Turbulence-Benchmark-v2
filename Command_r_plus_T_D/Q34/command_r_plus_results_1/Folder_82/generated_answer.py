def find_original_set(*sets):
    if len(sets) != 47:
        raise ValueError('Exactly 47 sets are required')
    if not all((isinstance(s, set) for s in sets)):
        raise TypeError('All arguments must be sets')
    if not all((all((isinstance(i, int) for i in s)) for s in sets)):
        raise TypeError('All set elements must be integers')
    original_set = set.union(*sets)
    return original_set