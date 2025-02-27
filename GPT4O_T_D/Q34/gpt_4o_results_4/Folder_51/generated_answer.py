def find_original_set(*sets):
    if len(sets) != 28:
        raise ValueError('Exactly 28 sets are required')
    result_set = set()
    for s in sets:
        result_set = result_set.union(s)
    return result_set