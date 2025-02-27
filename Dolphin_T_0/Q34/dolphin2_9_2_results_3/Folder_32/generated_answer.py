def find_original_set(*sets):
    result = sets[0]
    for set in sets[1:]:
        result |= set
    return result