def find_original_set(*sets):
    if len(sets) != 21:
        raise ValueError('Exactly 21 sets must be provided.')
    union_set = set()
    for s in sets:
        union_set.update(s)
    return union_set