def find_original_set(*sets):
    if len(sets) != 9:
        raise ValueError('Function requires exactly 9 sets')
    if len(set(map(len, sets))) != len(sets):
        raise ValueError('All sets must have distinct sizes')
    original_set = set()
    for s in sorted(sets, key=len):
        original_set.update(s)
    return original_set