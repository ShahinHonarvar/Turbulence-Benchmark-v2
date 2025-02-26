def find_original_set(*sets):
    if len(sets) != 16:
        raise ValueError('Exactly 16 sets must be provided')
    original_set = set()
    for s in sets:
        if not isinstance(s, set):
            raise TypeError('All arguments must be sets')
        original_set.update(s)
    return original_set