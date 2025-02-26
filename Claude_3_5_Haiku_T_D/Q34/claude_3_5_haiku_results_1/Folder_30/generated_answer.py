def find_original_set(*sets):
    if len(sets) != 78:
        raise ValueError('Function requires exactly 78 sets')
    result = set()
    for s in sets:
        result.update(s)
    return result