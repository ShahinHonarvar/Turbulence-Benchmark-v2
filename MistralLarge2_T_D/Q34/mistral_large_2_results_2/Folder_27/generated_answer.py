def find_original_set(*sets):
    if len(sets) != 100:
        raise ValueError('The function must take exactly 100 arguments.')
    result_set = set()
    for s in sets:
        if not isinstance(s, set):
            raise ValueError('All arguments must be sets.')
        result_set.update(s)
    return result_set