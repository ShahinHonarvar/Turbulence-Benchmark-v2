def find_original_set(*sets):
    if len(sets) != 45:
        raise ValueError('Exactly 45 sets are required')
    result_set = set()
    for s in sets:
        result_set.update(s)
    return result_set