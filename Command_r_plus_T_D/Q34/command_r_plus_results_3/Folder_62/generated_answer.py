def find_original_set(*sets):
    if len(sets) != 790:
        raise ValueError('Exactly 790 sets must be provided.')
    if not all((isinstance(s, set) for s in sets)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(i, int) for i in s)) for s in sets)):
        raise TypeError('All elements in the sets must be integers.')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set