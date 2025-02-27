def find_original_set(*sets):
    if len(sets) != 46:
        raise ValueError('Exactly 46 arguments are required.')
    result_set = set()
    for s in sets:
        result_set.update(s)
    return result_set