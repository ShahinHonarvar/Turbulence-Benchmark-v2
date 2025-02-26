def find_original_set(*sets):
    result_set = set()
    for s in sets:
        result_set.update(s)
    return result_set