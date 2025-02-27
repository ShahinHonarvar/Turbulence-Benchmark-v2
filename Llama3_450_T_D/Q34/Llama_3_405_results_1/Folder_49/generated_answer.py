def find_original_set(*sets):
    if len(sets) != 60:
        raise ValueError('Exactly 60 sets must be provided')
    if not all((isinstance(s, set) for s in sets)):
        raise ValueError('All arguments must be sets')
    if not all((len(s) == len(set(s)) for s in sets)):
        raise ValueError('All sets must contain distinct integers')
    return set.union(*sets)