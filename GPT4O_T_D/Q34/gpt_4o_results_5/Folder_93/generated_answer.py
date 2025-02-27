def find_original_set(*sets):
    if len(sets) != 90:
        raise ValueError('The function requires exactly 90 arguments.')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set