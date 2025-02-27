def find_original_set(*sets):
    if len(sets) != 790:
        raise ValueError('Exactly 790 sets are required.')
    result_set = set()
    for s in sets:
        result_set.update(s)
    return result_set