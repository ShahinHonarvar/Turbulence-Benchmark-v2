def find_original_set(sets):
    result = set()
    for s in sets:
        result.update(s)
    return result