def find_original_set(*sets):
    if len(sets) != 57:
        raise ValueError('Exactly 57 sets must be provided')
    union_set = set()
    for s in sets:
        if not isinstance(s, set):
            raise ValueError('All arguments must be sets of integers')
        union_set.update(s)
    return union_set