def find_original_set(*sets):
    if len(sets) != 45:
        raise ValueError('The function should take exactly 45 arguments.')
    min_set = set()
    for s in sets:
        if not s.issubset(min_set):
            min_set = s
    return min_set