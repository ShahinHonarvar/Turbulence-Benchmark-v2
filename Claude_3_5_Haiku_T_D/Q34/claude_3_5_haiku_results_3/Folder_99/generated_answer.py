def find_original_set(*sets):
    if len(sets) != 415:
        raise ValueError('Function requires exactly 415 sets as arguments')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set