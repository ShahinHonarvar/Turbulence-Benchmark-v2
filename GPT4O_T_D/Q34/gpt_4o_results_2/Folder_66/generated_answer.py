def find_original_set(*sets):
    if len(sets) != 25:
        raise ValueError('The function requires exactly 25 arguments.')
    result_set = set()
    for s in sets:
        result_set.update(s)
    return result_set