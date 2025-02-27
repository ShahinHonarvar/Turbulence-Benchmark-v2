def find_original_set(*sets):
    if len(sets) != 78:
        raise ValueError('Exactly 78 sets must be provided')
    result = set()
    for s in sets:
        result.update(s)
    return result