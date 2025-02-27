def find_original_set(*sets):
    result = None
    for s in sets:
        if result is None:
            result = s
        else:
            result = result.union(s)
    return result