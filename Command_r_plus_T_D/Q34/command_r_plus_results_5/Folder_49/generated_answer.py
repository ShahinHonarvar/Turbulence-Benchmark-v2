def find_original_set(*sets):
    if len(sets) != 60:
        raise ValueError('Exactly 60 sets are required')
    if not all((isinstance(s, set) for s in sets)):
        raise TypeError('All arguments must be sets')
    if not all((all((isinstance(i, int) for i in s)) for s in sets)):
        raise TypeError('All elements in sets must be integers')
    original_set = set.union(*sets)
    return original_set