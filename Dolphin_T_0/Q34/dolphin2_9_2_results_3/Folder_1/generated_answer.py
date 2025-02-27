def find_original_set(*sets):
    result = set()
    for set_ in sets:
        result = result.union(set_)
    return result