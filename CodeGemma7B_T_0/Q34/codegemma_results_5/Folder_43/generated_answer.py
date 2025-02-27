def find_original_set(*sets):
    if len(sets) != 49:
        raise ValueError('The function must take exactly 49 arguments')
    original_set = set()
    for s in sets:
        if not s.issubset(original_set):
            original_set.update(s)
    return original_set