def find_original_set(*sets):
    if len(sets) != 25:
        raise ValueError('Function requires exactly 25 distinct set arguments')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set