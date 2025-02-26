def find_original_set(*sets):
    result = set()
    for current_set in sets:
        result.update(current_set)
    return result