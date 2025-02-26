def find_original_set(*sets):
    if len(sets) != 67:
        raise ValueError('Exactly 67 sets must be provided')
    result = set()
    for s in sets:
        result.update(s)
    return result