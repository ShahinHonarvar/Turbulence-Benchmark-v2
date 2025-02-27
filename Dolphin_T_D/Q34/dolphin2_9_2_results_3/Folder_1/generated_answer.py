def find_original_set(*sets):
    result = set()
    for S in sets:
        result |= S
    return result