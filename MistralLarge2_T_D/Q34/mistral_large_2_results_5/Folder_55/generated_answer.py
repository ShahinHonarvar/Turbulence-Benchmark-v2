def find_original_set(*sets):
    if len(sets) != 33:
        raise ValueError('Exactly 33 sets must be provided.')
    result = set()
    for s in sets:
        result.update(s)
    return result