def find_original_set(*sets):
    if len(sets) != 990:
        raise ValueError('Function requires exactly 990 distinct set arguments')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set