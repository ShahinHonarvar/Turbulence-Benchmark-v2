def find_original_set(*sets):
    if len(sets) != 63:
        raise ValueError('Function requires exactly 63 sets')
    union_set = set()
    for s in sets:
        union_set.update(s)
    return union_set