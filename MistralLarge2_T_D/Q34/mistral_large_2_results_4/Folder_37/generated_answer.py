def find_original_set(*sets):
    assert len(sets) == 67, 'Exactly 67 sets must be provided.'
    union_set = set()
    for s in sets:
        union_set.update(s)
    return union_set