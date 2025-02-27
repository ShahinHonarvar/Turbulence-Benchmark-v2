def find_original_set(*sets):
    if len(sets) != 37:
        raise ValueError('Exactly 37 arguments are required.')
    union_set = set()
    for s in sets:
        union_set.update(s)
    return union_set