def find_original_set(*sets):
    if len(sets) != 321:
        raise ValueError('Exactly 321 sets are required.')
    result = set()
    for s in sets:
        result.update(s)
    return result