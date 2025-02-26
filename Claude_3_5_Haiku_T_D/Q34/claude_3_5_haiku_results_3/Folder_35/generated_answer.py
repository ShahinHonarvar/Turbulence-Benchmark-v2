def find_original_set(*sets):
    if len(sets) != 702:
        raise ValueError('Function must be called with exactly 702 sets')
    result = set()
    for s in sets:
        result.update(s)
    return result