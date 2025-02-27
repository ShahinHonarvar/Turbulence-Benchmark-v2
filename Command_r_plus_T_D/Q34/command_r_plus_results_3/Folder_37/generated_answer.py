def find_original_set(*sets):
    if len(sets) != 67:
        raise ValueError('Exactly 67 sets are required.')
    if not all((isinstance(s, set) for s in sets)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(i, int) for i in s)) for s in sets)):
        raise TypeError('All elements in the sets must be integers.')
    if not all((sets[i].issubset(sets[i + 1]) for i in range(66))):
        raise ValueError('Each set must be a subset of the next one.')
    original_set = set.union(*sets)
    return original_set