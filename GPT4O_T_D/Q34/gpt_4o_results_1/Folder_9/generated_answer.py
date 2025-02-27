def find_original_set(*sets):
    if len(sets) != 73:
        raise ValueError('The function requires exactly 73 sets as arguments.')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set