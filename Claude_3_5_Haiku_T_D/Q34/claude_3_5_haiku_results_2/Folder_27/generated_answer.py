def find_original_set(*sets):
    if len(sets) != 100:
        raise ValueError('Function requires exactly 100 sets')
    result_set = set()
    for s in sets:
        result_set.update(s)
    return result_set