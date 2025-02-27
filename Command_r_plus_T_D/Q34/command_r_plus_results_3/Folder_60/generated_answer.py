def find_original_set(*sets):
    if len(sets) != 35:
        raise ValueError('Exactly 35 sets are required as input.')
    original_set = set()
    for s in sets:
        if not isinstance(s, set):
            raise TypeError('All inputs must be sets.')
        original_set = original_set.union(s)
    return original_set