def find_original_set(*sets):
    result = set()
    for subset in sets:
        result.update(subset)
    return result