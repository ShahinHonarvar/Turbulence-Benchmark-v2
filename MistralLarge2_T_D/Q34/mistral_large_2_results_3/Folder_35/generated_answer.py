def find_original_set(*sets):
    if len(sets) != 702:
        raise ValueError('Exactly 702 arguments are required')
    result = set()
    for s in sets:
        result.update(s)
    return result